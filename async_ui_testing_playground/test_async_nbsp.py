import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_nbsp(page: Page):
  await page.goto("http://uitestingplayground.com/nbsp", wait_until="networkidle")

  # Look on https://en.wikipedia.org/wiki/List_of_Unicode_characters
  # to figure out which unicode character matches to the HTML character
  btn = page.locator("//button[text()='My\u00a0Button']")
  await expect(btn).to_be_visible()