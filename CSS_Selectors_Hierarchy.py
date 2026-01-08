from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=3500)
    
    #create a new page
    page=browser.new_page()

  # Visit the Bootswatch website
    page.goto("https://bootswatch.com/default")

    # Visually highlight the active nav link
    page.locator("nav.bg-dark a.nav-link.active").evaluate(
        "el => el.style.outline = '4px solid red'"
    )

    # Keep browser open for inspection
    page.pause()

    page.locator("h1:text('Navbar')").highlight()