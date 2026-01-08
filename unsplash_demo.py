from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2500)
    
    #create a new page
    page=browser.new_page()

    # visit the Bootswatch website 
    page.goto("https:/unsplash.com")
    page.get_by_alt_text("a group of people sitting arround a table with food").highlight()

    # # Locating with CSS Selectors
    # page.locator("css=h1").highlight()
    # page.locator("footer").highlight()