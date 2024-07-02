import re
from playwright.sync_api import Page, expect
import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

@pytest.mark.asyncio
async def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


# @pytest.mark.asyncio
# async def test_has_title():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto('https://www.google.com/maps')
#         assert "Google Maps" in await page.title()
#         await browser.close()

# @pytest.mark.asyncio
# async def test_get_started_link():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto('https://www.google.com/maps')
#         assert "Google Maps" in await page.title()
#         await browser.close()
