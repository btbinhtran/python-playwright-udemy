from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch()

  page = browser.new_page()
  page.goto("https://playwright.dev/python")

  link = page.get_by_role("link", name="GET STARTED")

  breakpoint()

  link.click()