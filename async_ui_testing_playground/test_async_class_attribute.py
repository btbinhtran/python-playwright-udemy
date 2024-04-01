import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_class_attribute(page: Page):
    await page.goto("http://uitestingplayground.com/classattr")
    
    primary_btn = page.locator("button.btn-primary")

    await expect(primary_btn).to_be_visible()

    await primary_btn.click()
