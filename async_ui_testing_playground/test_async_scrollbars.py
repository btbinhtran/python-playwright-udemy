import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_scrollbars(page: Page):
    await page.goto("http://uitestingplayground.com/scrollbars")
    hiding_btn = page.get_by_role("button", name="Hiding Button")

    await hiding_btn.click()
    await page.screenshot(path="test_async_scrollbars.png")
    await expect(hiding_btn).to_be_in_viewport()