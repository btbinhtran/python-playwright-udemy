from playwright.sync_api import sync_playwright


def on_dialog(dialog):
  print("Dialog opened:", dialog)
  # This is to handle the prompt dialog that asks for input
  dialog.accept("Playwright is cool")
  # dialog.accept()
  # dialog.dismiss()


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(
    headless=False, slow_mo=1000
  )
  page = browser.new_page()
  page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

  page.on("dialog", on_dialog)

  alert_btn = page.get_by_text("Show alert box")
  alert_btn.click()

  confirm_btn = page.get_by_text("Show confirm box")
  confirm_btn.click()

  prompt_btn = page.get_by_text("Show prompt box")
  prompt_btn.click()

  browser.close()