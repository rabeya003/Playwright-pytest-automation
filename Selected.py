from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=350)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default", wait_until="domcontentloaded")

    select = page.get_by_label("Example select")
    select.scroll_into_view_if_needed()
    select.select_option("4")  # single-select: last call wins
    select.select_option("5")  
    page.wait_for_timeout(2000)

    multi_select = page.get_by_label("Example multiple select")
    multi_select.scroll_into_view_if_needed()
    multi_select.select_option(["2", "3", "1"])  # multi-select
    multi_select.select_option(["1", "3", "5"]) (["2", "4", "5"]) 

    page.pause()  
