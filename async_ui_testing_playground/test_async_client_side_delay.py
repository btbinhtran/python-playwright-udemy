import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_client_side_delay(page: Page):
  await page.goto("http://uitestingplayground.com/clientdelay")

  btn = page.get_by_role("button", name="Button Triggering Client Side Logic")
  await btn.click()

  paragraph = page.locator("p.bg-success")
  await paragraph.wait_for()

  await expect(paragraph).to_be_visible()