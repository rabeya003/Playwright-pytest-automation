from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=500)
    #create a new page
    page=browser.new_page()


    browser.close()