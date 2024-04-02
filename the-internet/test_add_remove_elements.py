import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_add_remove_elements(page: Page):
  """
  Write a test script to add two elements and then remove one. Verify the remaining element count.
  Modify the script to handle errors when trying to remove a non-existent element.
  await page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
  """
  await page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

  add_element_btn = page.get_by_role("button", name="Add Element")
  await add_element_btn.click(click_count=2)

  delete_btns = page.get_by_role("button", name="Delete")

  await expect(delete_btns).to_have_count(2)

  await delete_btns.last.click()

  await expect(delete_btns).to_have_count(1)