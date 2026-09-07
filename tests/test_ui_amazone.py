import pytest
from playwright.sync_api import sync_playwright
import time

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Applewebkit/537.36 Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        yield page
        browser.close()

def test_amazon_title(page):
    page.goto("https://www.amazon.in", timeout=60000, wait_until="domcontentloaded")
    time.sleep(3)
    content = page.content().lower()
    title = page.title()
    print(f"Title found: {title}")
    assert "Amazon" in title.lower() or "amazon" in content or page.url.startswith("https://www.amazone")

