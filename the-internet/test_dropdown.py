import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_dropdown(page: Page):
  """
  Write a test to select a specific option (by text or value)
  from the dropdown menu and verify the selected option.
  """
  await page.goto("https://the-internet.herokuapp.com/dropdown")

  options = ["Option 1", "Option 2"]

  dropdown = page.locator("select#dropdown")

  for option in options:
    await dropdown.select_option(option)
    value = option.split()[-1]
    await expect(dropdown).to_have_value(value)