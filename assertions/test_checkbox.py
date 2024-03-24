from playwright.sync_api import Page, expect

def test_app(page: Page):
  page.goto("https://bootswatch.com/default")

  default_checkbox = page.get_by_label("Default checkbox")
  checked_checkbox = page.get_by_label("Checked checkbox")

  expect(checked_checkbox).to_be_checked()

  expect(default_checkbox).not_to_be_checked()