from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight active nav link
    page.locator("nav.bg-dark a.nav-link.active").evaluate(
        "el => el.style.outline = '4px solid red'"
    )

    # Highlight h1 with text "Navbar"
    page.locator("h1", has_text="Navbar").evaluate(
        "el => el.style.outline = '4px solid blue'"
    )

    # Open dropdown so it becomes visible
    page.locator("a.dropdown-toggle").click()

    # Highlight visible dropdown menu
    page.locator("div.dropdown-menu:visible").evaluate(
        "el => el.style.outline = '4px solid green'"
    )

    page.pause()
