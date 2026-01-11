from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    # Radio buttons (exact label text)
    radio_option1 = page.get_by_label("Option one is this and that—be sure to include why it's great").first
    radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one").first

    radio_option1.scroll_into_view_if_needed()
    radio_option1.check()
    radio_option2.check()  # switch selection


    page.wait_for_timeout(8000)
    browser.close()
