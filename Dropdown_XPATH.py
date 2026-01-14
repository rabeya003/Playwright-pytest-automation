from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    dropdown=page.locator("//button[@id='btnGroupDrop1']").click()  #Xpath
    page.wait_for_timeout(200)

    # page.locator("//div[@class='dropdown-menu show']//a[2]").highlight()
    # page.locator("div.dropdown-menu:visible").highlight()menu = page.locator("css=div.dropdown-menu.show")
    # Wait for the dropdown menu to be shown (XPath)
    menu = page.locator("xpath=//div[contains(@class,'dropdown-menu') and contains(@class,'show')]")
    menu.wait_for(state="visible")

    # Manual highlight (Playwright Python doesn't have .highlight())
    menu.evaluate("el => el.style.outline='3px solid red'")

    page.wait_for_timeout(2000)
