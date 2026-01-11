from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    primary = page.get_by_role("button", name="Primary")
    primary.first.wait_for(state="visible")   # ensure buttons are loaded

    primary.nth(0).scroll_into_view_if_needed(); primary.nth(0).highlight()
    primary.nth(1).scroll_into_view_if_needed(); primary.nth(1).highlight()
    primary.nth(2).scroll_into_view_if_needed(); primary.nth(2).highlight()

    page.wait_for_timeout(8000)
    browser.close()
