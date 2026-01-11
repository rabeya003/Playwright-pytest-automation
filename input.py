from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=3500)
    
    #create a new page
    page=browser.new_page()

    # visit the Bootswatch website 
    page.goto("https://bootswatch.com/default")
    input=page.get_by_placeholder("Enter email")

    input.fill("rabey.QAgmail.com")
    input.clear()
    input.type("rabey.QAgmail.com",delay=200)


    page.wait_for_timeout(8000)
    browser.close()