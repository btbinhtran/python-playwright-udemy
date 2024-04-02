import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_checkboxes(page: Page):
  """
  Initial states:
  * checkbox 1 is unchecked
  * checkbox 2 is checked
  """
  await page.goto("https://the-internet.herokuapp.com/checkboxes")

  checkbox1 = page.get_by_role("checkbox").first
  checkbox2 = page.get_by_role("checkbox").last

  await expect(checkbox1).not_to_be_checked()
  await expect(checkbox2).to_be_checked()

  await checkbox1.check()
  await checkbox2.uncheck()

  await expect(checkbox1).to_be_checked()
  await expect(checkbox2).not_to_be_checked()