from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    # visit the Bootswatch website
    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    email_input = page.get_by_placeholder("Enter email").first
    email_input.scroll_into_view_if_needed()
    email_input.fill("rabey.QAgmail.com")
    email_input.fill("")  # clear
    email_input.type("rabey.QAgmail.com", delay=200)

    # valid input (this is a label on the page; set and then read the value)
    valid_input = page.get_by_label("Valid input").first
    valid_input.scroll_into_view_if_needed()
    valid_input.fill("correct value")
    print("Valid input value:", valid_input.input_value())

    valid_input.fill("some other value")
    print("Valid input value:", valid_input.input_value())

    page.wait_for_timeout(8000)
    browser.close()
