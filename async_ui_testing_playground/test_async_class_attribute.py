import pytest
from playwright.async_api import async_playwright, expect


@pytest.fixture(autouse=True)
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Change browser if needed
        yield browser
        await browser.close()


@pytest.fixture(autouse=True)
async def page(browser):
    async for b in browser:
      page = await b.new_page()
      yield page
      await page.close()


@pytest.mark.asyncio
async def test_async_class_attribute(page):
    async for p in page:
      await p.goto("http://uitestingplayground.com/classattr")
      
      primary_btn = p.locator("button.btn-primary")

      await expect(primary_btn).to_be_visible()

      await primary_btn.click()