from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False, slow_mo=500)

  page = browser.new_page()
  page.goto("https://playwright.dev/python")

  page.evaluate("window.scrollBy(0, document.body.scrollHeight)")

  page.screenshot(path="end.jpg")