import pytest
from playwright.async_api import Page, TimeoutError

@pytest.mark.asyncio
async def test_async_hidden(page: Page):
  await page.goto("http://uitestingplayground.com/hiddenlayers", wait_until="networkidle")

  green_btn = page.locator("button#greenButton")

  await green_btn.click()

  # checking that you cannot click on the green button twice
  with pytest.raises(TimeoutError):
    await green_btn.click(timeout=2000)