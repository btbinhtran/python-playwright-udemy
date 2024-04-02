import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_overlapped_element(page: Page):
  await page.goto("http://uitestingplayground.com/overlapped")

  name_input = page.get_by_placeholder("Name")

  div = name_input.locator("..")
  await div.hover()

  await page.mouse.wheel(0, 200)

  expected_name = "Poolsnake"
  await name_input.fill(expected_name)

  await div.screenshot(path="test_async_overlapped_element.png")

  await expect(name_input).to_have_value(expected_name)

