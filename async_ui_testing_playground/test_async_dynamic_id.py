import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_dynamic_id():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role(
      "button", name="Button with Dynamic ID"
    )
    await expect(button).to_be_visible()
    await button.click()