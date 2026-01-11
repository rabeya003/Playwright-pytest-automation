from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()

    def highlight_if_found(locator, name: str):
        if locator.count() > 0:
            locator.first.scroll_into_view_if_needed()
            locator.first.highlight()
        else:
            print(f"Not found: {name}")

    try:
        page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

        highlight_if_found(page.locator("xpath=//h1"), "//h1")
        highlight_if_found(page.locator("#navbar"), "#navbar (nav)")
        highlight_if_found(page.locator("xpath=//input[@readonly]"), "//input[@readonly]")

        wrong = page.locator("xpath=//input[@value='wrong value']")
        highlight_if_found(wrong, "//input[@value='wrong value']")

        highlight_if_found(page.locator("xpath=//h1[contains(normalize-space(.), 'Head')]"),
                           "//h1[contains(.,'Head')]")
        highlight_if_found(page.locator("xpath=//button[contains(@class,'btn-outline-primary')]"),
                           "//button[contains(@class,'btn-outline-primary')]")

        page.wait_for_timeout(8000)

    finally:
        browser.close()
