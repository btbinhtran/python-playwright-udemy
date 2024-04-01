import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_load_delay(page: Page):
  await page.goto("http://uitestingplayground.com")

  load_delay_link = page.get_by_role("link", name="Load Delay")
  await load_delay_link.click()

  btn = page.get_by_role("button", name="Button Appearing After Delay")

  await btn.wait_for(timeout=10_000)

  await expect(btn).to_be_visible()