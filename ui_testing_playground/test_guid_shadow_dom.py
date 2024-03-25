import pytest
import asyncio
from playwright.async_api import async_playwright, Page, expect

@pytest.mark.asyncio
async def test_guid_shadow_dom():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False, slow_mo=500)
    context = await browser.new_context(
      permissions=["clipboard-read", "clipboard-write"]
    )
    page = await context.new_page()
    await page.goto("http://uitestingplayground.com/shadowdom")

    setting_btn = page.locator("button#buttonGenerate")
    copy_btn = page.locator("button#buttonCopy")
    edit_field = page.locator("input#editField")

    await expect(edit_field).to_be_empty()

    await setting_btn.click()
    await expect(edit_field).not_to_be_empty()

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
    await page.evaluate("document.getElementById('CLIP').remove();")

    edit_field = page.locator("input#editField")
    await expect(edit_field).to_have_value(clipboard_value)

    await browser.close()