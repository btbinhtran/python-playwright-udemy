import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_progressbar(page: Page):
  await page.goto("http://uitestingplayground.com/progressbar", wait_until="networkidle")
  stop_percentage = 75
  value_now = None

  progressbar = page.get_by_role("progressbar")

  start_btn = page.get_by_role("button", name="Start")
  stop_btn = page.get_by_role("button", name="Stop")

  await start_btn.click()

  while True:
    valuenow = int(await progressbar.get_attribute("aria-valuenow"))

    if valuenow >= stop_percentage:
      break
    else:
      print(f"Percent: {valuenow}%")

  await stop_btn.click()

  assert valuenow >= stop_percentage