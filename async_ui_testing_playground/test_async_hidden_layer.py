import asyncio
import playwright
import pytest, pytest_asyncio
from playwright.async_api import TimeoutError, expect

@pytest.mark.asyncio
async def test_async_hidden(page):
  await page.goto("http://uitestingplayground.com/hiddenlayers")

  green_btn = page.locator("button#greenButton")

  await green_btn.click()

  # checking that you cannot click on the green button twice
  with pytest.raises(TimeoutError):
    await green_btn.click(timeout=2000)