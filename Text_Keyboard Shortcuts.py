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
    textarea.type("Sabbir Hossain,,, Sales & Marketing", delay=200)

    # Pause so you can see the text
    page.wait_for_timeout(800)

    # Clear like a user (slowly)
    textarea.press("Control+A")
    page.wait_for_timeout(300)
    textarea.press("Backspace")
    page.wait_for_timeout(500)

    # Press keys slowly so you can see what happens
    textarea.press("KeyW")
    page.wait_for_timeout(300)
    textarea.press("KeyO")
    page.wait_for_timeout(300)
    textarea.press("KeyR")
    page.wait_for_timeout(300)
    textarea.press("Shift+KeyD")
    page.wait_for_timeout(500)

    textarea.press("Control+ArrowLeft")
    page.wait_for_timeout(500)
    textarea.press("ArrowRight")
    page.wait_for_timeout(1500)

    browser.close()
