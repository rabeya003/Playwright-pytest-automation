from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=1200)
    
    #create a new page
    page=browser.new_page()

    # visit the Bootswatch website 
    page.goto("https://bootswatch.com/default")
    btn=page.get_by_role('button',name="Default button")
    btn.highlight()
    btn.click()

    
