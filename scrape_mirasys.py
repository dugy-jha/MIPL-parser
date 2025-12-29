import asyncio
import os
import re
import json
import signal
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright, Page

# Configuration
START_URL = "https://documentation.mirasys.com/"
OUTPUT_DIR = "mirasys_docs"
STATE_FILE = "scraper_state.json"
CONCURRENCY = 5

# Configuration
START_URL = "https://documentation.mirasys.com/"
OUTPUT_DIR = "mirasys_docs"
STATE_FILE = "scraper_state.json"
CONCURRENCY = 5

# History from previous runs (persistent)
history_urls = set()
# Visited in THIS run (transient, for loop prevention)
visited_session_urls = set()
# Queue for URLs to visit
urls_to_visit = asyncio.Queue()

def load_state():
    """Load state from JSON file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                history_urls.update(data.get("visited", []))
                # We do NOT load the queue if we want to force re-crawl from root to recover frontier.
                # But if we have a valid queue, we should use it.
                # In our case, queue is [ROOT], so it's fine.
                saved_queue = data.get("queue", [])
                if saved_queue:
                    for url in saved_queue:
                        urls_to_visit.put_nowait(url)
                else:
                    urls_to_visit.put_nowait(START_URL)
                    
            print(f"Loaded state: {len(history_urls)} in history, {urls_to_visit.qsize()} in queue.")
        except Exception as e:
            print(f"Error loading state: {e}")
            urls_to_visit.put_nowait(START_URL)
    else:
        urls_to_visit.put_nowait(START_URL)

async def save_state_async():
    """Save current queue and visited to file."""
    # Snapshot queue
    queue_items = []
    size = urls_to_visit.qsize()
    for _ in range(size):
        item = urls_to_visit.get_nowait()
        queue_items.append(item)
        urls_to_visit.put_nowait(item)
        urls_to_visit.task_done()
    
    data = {
        "visited": list(history_urls),
        "queue": queue_items
    }
    # Temp write
    with open(STATE_FILE + ".tmp", "w", encoding="utf-8") as f:
        json.dump(data, f)
    os.replace(STATE_FILE + ".tmp", STATE_FILE)
    # print("State saved.")

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

async def save_page_content(page_url, title, content):
    try:
        parsed_url = urlparse(page_url)
        path_parts = parsed_url.path.strip('/').split('/')
        
        if not path_parts:
            filename = "index"
        else:
            filename = path_parts[-1]
            if not filename:
                filename = "index"
        
        if len(path_parts) > 1:
            guide_dir = os.path.join(OUTPUT_DIR, sanitize_filename(path_parts[0]))
        else:
            guide_dir = OUTPUT_DIR
            
        os.makedirs(guide_dir, exist_ok=True)
        file_path = os.path.join(guide_dir, f"{sanitize_filename(filename)}.md")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"Source: {page_url}\n\n")
            f.write(content)
        return True
        
    except Exception as e:
        print(f"Error saving {page_url}: {e}")
        return False

async def process_url(context, url):
    if url in visited_session_urls:
        return
    
    visited_session_urls.add(url) # Mark as visited in this session

    # Optimization: If it's in history, do we need to visit it?
    # YES, to extract links. We can't know the links otherwise.
    # UNLESS we saved links in history (we didn't).
    
    page: Page = await context.new_page()
    try:
        print(f"Visiting: {url}")
        await page.goto(url, timeout=60000)
        # Faster wait if possible?
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=10000)
        except:
             pass # proceed anyway
        
        # Only extract/save content if NOT in history
        if url not in history_urls:
            title = await page.title()
            content = await page.evaluate("""() => {
                const article = document.querySelector('article') || document.querySelector('main') || document.body;
                return article.innerText; 
            }""")
            if await save_page_content(url, title, content):
                history_urls.add(url)
                print(f"Saved new: {url}")
        else:
            # print(f"Skipped saving (already in history): {url}")
            pass
        
        # ALWAYS extract links to rebuild frontier
        links = await page.evaluate("""() => {
            const anchors = Array.from(document.querySelectorAll('a'));
            return anchors.map(a => a.href);
        }""")
        
        for link in links:
            if link.startswith("https://documentation.mirasys.com/"):
                if "#" not in link and not link.endswith(".pdf"):
                     if link not in visited_session_urls:
                         urls_to_visit.put_nowait(link)
                     
    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        await page.close()

async def worker(context):
    while True:
        try:
            url = urls_to_visit.get_nowait()
        except asyncio.QueueEmpty:
            break
            
        if url in visited_session_urls:
            urls_to_visit.task_done()
            continue
            
        await process_url(context, url)
        urls_to_visit.task_done()
        
        # Periodic save (every 10 urls processed)
        if len(visited_session_urls) % 10 == 0:
             await save_state_async()

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    load_state()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        workers = [asyncio.create_task(worker(context)) for _ in range(CONCURRENCY)]
        
        # Monitor loop
        while not urls_to_visit.empty() or any(not w.done() for w in workers):
            await asyncio.sleep(5)
            await save_state_async()
            
            if urls_to_visit.empty():
                 await asyncio.sleep(2)
                 if urls_to_visit.empty():
                     break
                     
        for w in workers:
            w.cancel()
            
        await save_state_async() # Final save
        await browser.close()


def dummy_handler(signum, frame):
    print("Received stop signal. State will be saved by main loop or on exit logic.")
    # We rely on the async loop to handle cleanup or KeyboardInterrupt
    raise KeyboardInterrupt

if __name__ == "__main__":
    signal.signal(signal.SIGINT, dummy_handler)
    signal.signal(signal.SIGTERM, dummy_handler)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping... Saving state.")
        # We need to run save_state_async which is async, but we are out of loop.
        # Actually, `visited_urls` and `urls_to_visit` are global.
        # We can implement a synchronous save or run a quick loop.
        
        # Sync save for safety
        queue_items = []
        while not urls_to_visit.empty():
            queue_items.append(urls_to_visit.get_nowait())
            
        data = {
            "visited": list(visited_urls),
            "queue": queue_items
        }
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
        print("State saved to scraper_state.json")
