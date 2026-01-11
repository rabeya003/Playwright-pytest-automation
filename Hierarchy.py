from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    nav_active = page.locator("nav.bg-dark a.nav-link.active")
    nav_active.first.wait_for(state="visible")
    nav_active.first.scroll_into_view_if_needed()
    nav_active.first.evaluate("el => el.style.outline='4px solid red'")

    navbar_h1 = page.locator("h1", has_text="Navbar")
    navbar_h1.first.scroll_into_view_if_needed()
    navbar_h1.first.evaluate("el => el.style.outline='4px solid blue'")

    dropdown = page.locator("a.dropdown-toggle").first
    dropdown.scroll_into_view_if_needed()
    dropdown.click()

    menu = page.locator("div.dropdown-menu")
    menu.first.wait_for(state="visible")
    menu.first.evaluate("el => el.style.outline='4px solid green'")

    page.pause()  # opens Inspector when PWDEBUG=1

