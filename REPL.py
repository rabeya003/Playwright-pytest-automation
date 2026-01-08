from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=1500)
    
    #create a new page
    page=browser.new_page()

    # visit the Bootswatch website 
    page.goto("https://bootswatch.com/default")
    btn=page.get_by_role('button',name="Default button")
    btn.highlight()
    btn.click()

    # ROLE
    #Radio btn 
    radio_btn=page.get_by_role('radio',name="Option one is this and that-be sure to include why it's great")
    radio_btn.highlight()
    # Checkbox
    checkbox=page.get_by_role('checkbox',name="Default checkbox")
    checkbox.highlight()
    checkbox.check()


    # Label & Email
    email_input=page.get_by_label("Email address")
    email_input.highlight()
    page.get_by_label("Password").highlight()
    page.get_by_label("Example textarea").highlight()

    page.get_by_placeholder('Enter email').highlight()
    page.get_by_placeholder("Password").highlight()

    # Text
    page.get_by_text("with muted text").highlight()
    page.get_by_text("Small button").highlight()
    page.get_by_text("Middle").click()

    page.get_by_text("fine print",exact=False).highlight()
    page.get_by_text("attr",exact=False).highlight()

