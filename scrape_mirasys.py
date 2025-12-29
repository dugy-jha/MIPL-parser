import asyncio
import os
import re
import json
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright, Page

# Configuration
START_URL = "https://documentation.mirasys.com/"
OUTPUT_DIR = "mirasys_docs"
STATE_FILE = "scraper_state.json"
CONCURRENCY = 5

# Set to keep track of visited URLs to avoid loops
visited_urls = set()
# Queue for URLs to visit
urls_to_visit = asyncio.Queue()

# Because asyncio.Queue is not easily serializable, we will use a set/list for saving the frontier.

def load_state():
    """Load state from JSON file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                visited_urls.update(data.get("visited", []))
                for url in data.get("queue", []):
                    urls_to_visit.put_nowait(url)
            print(f"Loaded state: {len(visited_urls)} visited, {urls_to_visit.qsize()} in queue.")
        except Exception as e:
            print(f"Error loading state: {e}")
    else:
        urls_to_visit.put_nowait(START_URL)

def save_state():
    """Save state to JSON file."""
    # Enhance: Drain queue to list, save, then put back? 
    # Or just copy. Queue doesn't support iteration easily.
    # We will rely on extracting items.
    # THIS IS TRICKY with async queue. 
    # Only safe way to snapshot a running async queue is if we are the only consumer/producer at that moment.
    # This function will primarily be called on exit or periodically.
    
    queue_list = []
    # This is a bit hacky for asyncio.Queue, but for snapshotting:
    # We can't iterate the queue easily.
    # Let's just track the 'frontier' set separately or rebuild it.
    pass 
    # Actually, simpler: write visited to disk immediately. 
    # Keep queue in memory. If we stop, we lose the queue.
    # Resuming just from 'visited' requires re-crawling the visited pages to find children again? 
    # Yes, typically.
    # UNLESS we treat the 'queue' file as our persistence.
    pass

# Simplified Approach for Robust Resume:
# 1. visited.txt -> Append only.
# 2. queue.txt -> Rewrite periodically? 
# 
# Let's go with:
# On START: Load visited.txt. 
# We add START_URL to queue. 
# When processing URL:
#   If valid link:
#     If link NOT in visited:
#       Add to queue.
#     If link IS in visited:
#       Ignore.
#
# BUT if we crushed in the middle, we have a bunch of pages in the queue that are NOT in visited.
# We lost them.
# So we need to recover the frontier.
# We can recover the frontier by re-scanning the last few visited pages? Or all?
# 
# Let's change the script to:
# 1. `visited_urls` populated from file on start.
# 2. `urls_to_visit` initialized with START_URL.
# 3. When `process_url` runs:
#    If url is in `visited_urls`:
#       Check if we need to re-scan for links (i.e. if we are "re-hydrating" the queue).
#       BUT we don't know if we finished scanning it.
#       
#       Actually, simpler:
#       Just save the queue to `queue.json` on graceful exit (signal handler).
#       And load it on start.
#       And also periodic save?

import signal

async def save_state_async():
    """Save current queue and visited to file."""
    # Snapshot queue
    queue_items = []
    size = urls_to_visit.qsize()
    for _ in range(size):
        item = urls_to_visit.get_nowait()
        queue_items.append(item)
        urls_to_visit.put_nowait(item) # Put back!
        urls_to_visit.task_done()
    
    data = {
        "visited": list(visited_urls),
        "queue": queue_items
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)
    print("State saved.")

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
        # print(f"Saved: {file_path}") # Reduce noise
        
    except Exception as e:
        print(f"Error saving {page_url}: {e}")

async def process_url(context, url):
    if url in visited_urls:
        return
    
    # Mark as visited tentatively (or after success)
    # We'll mark here to avoid loops
    visited_urls.add(url)

    page: Page = await context.new_page()
    try:
        print(f"Visiting: {url}")
        await page.goto(url, timeout=60000)
        await page.wait_for_load_state("networkidle")
        
        title = await page.title()
        
        content = await page.evaluate("""() => {
            const article = document.querySelector('article') || document.querySelector('main') || document.body;
            return article.innerText; 
        }""")
        
        await save_page_content(url, title, content)
        
        links = await page.evaluate("""() => {
            const anchors = Array.from(document.querySelectorAll('a'));
            return anchors.map(a => a.href);
        }""")
        
        for link in links:
            if link.startswith("https://documentation.mirasys.com/") and link not in visited_urls:
                if "#" not in link and not link.endswith(".pdf"):
                     # Add to queue only if not already there? (hard to check efficiently in async queue without set)
                     # We'll rely on visited check in worker
                     urls_to_visit.put_nowait(link)
                     
    except Exception as e:
        print(f"Error processing {url}: {e}")
        # If error, maybe remove from visited so we retry?
        visited_urls.discard(url)
    finally:
        await page.close()

async def worker(context):
    while True:
        try:
            url = urls_to_visit.get_nowait()
        except asyncio.QueueEmpty:
            break
            
        if url in visited_urls:
            urls_to_visit.task_done()
            continue
            
        await process_url(context, url)
        urls_to_visit.task_done()
        
        # Periodic save (inefficient but safe for simple script)
        if len(visited_urls) % 10 == 0:
            await save_page_content_dummy() # Hack: Actually just a placeholder. 
            # We won't save state in worker loop to avoid concurrency issues easily.
            pass

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
            # Periodic save?
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
