import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_text_input(page: Page):
  await page.goto("http://uitestingplayground.com/textinput")

  new_button_name = "COOL BUTTON DUDE!"

  input = page.get_by_placeholder("MyButton")
  btn = page.locator("button#updatingButton")
  
  await input.fill(new_button_name)
  await btn.click()

  await expect(btn).to_have_text(new_button_name)
  await expect(input).to_have_value(new_button_name)