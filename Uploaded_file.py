from pathlib import Path
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="networkidle")

    file_input = page.get_by_label("Default file input example")

    # Scroll to the file input location on the page
    file_input.scroll_into_view_if_needed()
    file_input.wait_for(state="visible")

    # Use an absolute path so it works reliably in VS Code
    file_path = Path("Hierarchy.py").resolve()
    file_input.set_input_files(str(file_path))

    page.wait_for_timeout(2000)
    browser.close()
