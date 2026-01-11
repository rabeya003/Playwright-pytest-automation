from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()

    try:
        page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

        # Use plain XPath (no 'xpath=' prefix needed when selector starts with //)
        page.locator("//h1").first.highlight()
        page.locator("//h1[@id='navbar']").highlight()
        page.locator("//input[@readonly]").first.highlight()
        page.wait_for_timeout(8000)


        # This one likely matches nothing; don't call highlight() if count == 0
        wrong = page.locator("//input[@value='wrong value']")
        if wrong.count() > 0:
            wrong.first.highlight()
        else:
            print("No element found for //input[@value='wrong value']")

        page.wait_for_timeout(8000)

    finally:
        browser.close()
