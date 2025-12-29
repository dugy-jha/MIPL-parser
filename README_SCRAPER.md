# Mirasys Documentation Scraper

This is a browser-based automation script to gather documentation details from [https://documentation.mirasys.com/](https://documentation.mirasys.com/).

## Prerequisites

You need Python 3.7+ installed.

## Installation

1.  **Install the required Python packages:**
    ```bash
    pip install playwright
    ```

2.  **Install the Playwright browsers:**
    ```bash
    playwright install chromium
    ```

## Usage

Run the script using Python:

```bash
python scrape_mirasys.py
```

## Output

The script will create a `mirasys_docs` directory and save the documentation pages as Markdown files, organized by section.

## Notes
- The script uses `asyncio` and `playwright` for high-performance scraping.
- It is configured to run with a concurrency of 5 tabs. You can adjust `CONCURRENCY` in the script if needed.
