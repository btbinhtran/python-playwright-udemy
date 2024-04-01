import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_ajax(page: Page):
  await page.goto("http://uitestingplayground.com/ajax")
  
  btn = page.get_by_role("button", name="Button Triggering AJAX Request")
  await btn.click()

  paragraph = page.locator("p.bg-success")
  await paragraph.wait_for()

  await expect(paragraph).to_be_visible()
