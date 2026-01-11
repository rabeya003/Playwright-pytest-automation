from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2500)
    page = browser.new_page()

    page.goto("https://unsplash.com", wait_until="domcontentloaded")

    # Unsplash changes often, so use a safer selector (example: search box)
    page.locator('input[type="search"]').first.scroll_into_view_if_needed()
    page.locator('input[type="search"]').first.highlight()

    page.wait_for_timeout(8000)
    browser.close()
