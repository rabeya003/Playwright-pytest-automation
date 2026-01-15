from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

PHOTO_ID = "0CL5pgXi1wQ"
PHOTO_URL = f"https://unsplash.com/photos/{PHOTO_ID}"
SAVE_AS = "unsplash_photo.jpg"

def step(page, text, seconds=2):
    print(f"\n=== {text} ===")
    page.wait_for_timeout(seconds * 1000)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=700)  # slow actions
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # 1) Go to Unsplash home
    step(page, "STEP 1: Open Unsplash home", 1)
    page.goto("https://unsplash.com", wait_until="domcontentloaded")
    step(page, "Home opened (pause to see page)", 4)

    # 2) Try cookie popup (if it exists)
    step(page, "STEP 2: Handle cookie popup if it shows", 1)
    try:
        # Different regions show different button text.
        # We try a few common ones.
        for btn_name in ["Accept all", "Accept All", "Accept", "I agree", "Agree"]:
            btn = page.get_by_role("button", name=btn_name)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click()
                step(page, f"Clicked cookie button: {btn_name}", 2)
                break
    except:
        step(page, "No cookie popup detected", 2)

   
    browser.close()
