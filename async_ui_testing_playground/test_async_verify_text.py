import pytest, re
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_verify_text(page: Page):
  await page.goto("http://uitestingplayground.com/verifytext", wait_until="networkidle")

  welcome_text = page.locator("div.bg-primary").get_by_text("Welcome")

  await expect(welcome_text).to_have_text("Welcome UserName!")