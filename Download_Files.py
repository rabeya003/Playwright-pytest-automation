from playwright.sync_api import sync_playwright

PHOTO_URL = "https://unsplash.com/photos/girl-opening-chicken-coop-door-with-hens-nearby-0CL5pgXi1wQ"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    response = page.goto(PHOTO_URL, wait_until="networkidle")
    print("Status:", response.status)
    print("Final URL:", page.url)

    # Sometimes cookie popup blocks clicks. Try to accept if it exists.
    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except:
        pass


    download_link = page.get_by_role("link", name="Download free").first
    download_link.wait_for(state="visible", timeout=15000)

    # Try to catch a real file download
    try:
        with page.expect_download(timeout=15000) as d:
            download_link.click()
        download = d.value
        file_path = download.path()  # temp file path
        download.save_as("unsplash_photo.jpg")
        print("Downloaded to: unsplash_photo.jpg")
    except:
        # Fallback: sometimes it opens a new tab instead of a direct download
        with context.expect_page(timeout=15000) as new_tab_info:
            download_link.click()
        new_page = new_tab_info.value
        new_page.wait_for_load_state("networkidle")
        print("Opened new tab URL:", new_page.url)

    browser.close()
