import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_guid_shadow_dom(page: Page):
  await page.goto("http://uitestingplayground.com/shadowdom")

  generate_btn = page.locator("button#buttonGenerate")
  copy_btn = page.locator("button#buttonCopy")
  edit_input = page.locator("input#editField")

  await expect(edit_input).to_be_empty()

  await generate_btn.click()
  await expect(edit_input).not_to_be_empty()

  await copy_btn.click()

  # Create input to paste element in
  await page.evaluate('''() => {
    const input = document.createElement('input');
    input.setAttribute('id', 'CLIP');
    document.body.appendChild(input);
    input.focus();
  }''')
  clip_input = page.locator("input#CLIP")
  await clip_input.press("Control+KeyV")
  clipboard_value = await clip_input.input_value()

  # Remove created input element
  await page.evaluate("document.getElementById('CLIP').remove();")

  await expect(edit_input).to_have_value(clipboard_value)