import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_dynamic_id(page: Page):
  await page.goto("http://uitestingplayground.com/dynamicid")

  button = page.get_by_role(
    "button", name="Button with Dynamic ID"
  )
  await expect(button).to_be_visible()
  await button.click()