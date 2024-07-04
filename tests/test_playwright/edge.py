import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/maps/@22.38131,114.168639,11z?entry=ttu")
    page.locator("#searchboxinput").fill("HKU")
    page.locator("#searchboxinput").press("Enter")
    page.get_by_role("link", name="The University of Hong Kong (HKU)", exact=True).click()
    # page.get_by_role("button", name="Search nearby The University of Hong Kong (HKU)").click()
    # page.get_by_role("combobox", name="Search nearby The University of Hong Kong (HKU)").fill("Starbucks")

    time.sleep(120)
    page.close()



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
