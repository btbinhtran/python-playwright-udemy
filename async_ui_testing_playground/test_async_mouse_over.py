import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_mouse_over(page: Page):
  await page.goto("http://uitestingplayground.com/mouseover")

  click_me_link = page.get_by_title("Click me")
  await click_me_link.hover()
  
  click_me_active_link = page.get_by_title("Active Link")
  await click_me_active_link.click(click_count=2)
  
  click_count_span = page.locator("span#clickCount")
  await expect(click_count_span).to_have_text("2")
