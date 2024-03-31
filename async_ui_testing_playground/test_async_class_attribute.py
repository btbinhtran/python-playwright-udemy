import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_async_class_attribute():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("http://uitestingplayground.com/classattr")

    primary_btn = page.locator("button.btn-primary")

    await expect(primary_btn).to_be_visible()

    await primary_btn.click()