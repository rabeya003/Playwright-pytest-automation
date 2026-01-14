from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=350)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="networkidle")

    textarea = page.get_by_label("Example textarea")

    # Scroll to the textarea so you can see it
    textarea.scroll_into_view_if_needed()
    textarea.wait_for(state="visible")
    textarea.click()

    # Type slowly
    textarea.type("Rabeya Boshri", delay=200)

    # Pause so you can see the text
    page.wait_for_timeout(800)



    browser.close()
