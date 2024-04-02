import pytest
from playwright.async_api import Page, TimeoutError, expect

async def on_dialog(dialog):
  assert dialog.message == "You selected a context menu"
  await dialog.accept()

@pytest.mark.asyncio
async def test_context_menu(page: Page):
  await page.goto("https://the-internet.herokuapp.com/context_menu")
  page.on("dialog", on_dialog)
  box = page.locator("div#hot-spot")
  
  await box.click(button="right")

  await expect(box).to_be_visible()