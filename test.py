from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight the h1
    page.locator("h1").evaluate(
        "el => el.style.outline = '3px solid red'"
    )

    # Highlight the button
    page.locator("button.btn-outline-success").evaluate(
        "el => el.style.outline = '3px solid blue'"
    )

    page.pause()
