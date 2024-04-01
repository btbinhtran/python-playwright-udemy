import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_click_action(page: Page):
  await page.goto("http://uitestingplayground.com/click")

  btn = page.get_by_role("button", name="Button That Ignores DOM Click Event")
  
  await btn.click()

  await expect(btn).to_have_class("btn btn-success")
  await expect(btn).to_have_id("badButton")
