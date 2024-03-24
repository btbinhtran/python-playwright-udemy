from playwright.sync_api import Page, expect

def test_app(page: Page):
  page.goto("https://bootswatch.com/default")

  option_menu = page.get_by_label("Example select")

  # single select with multiple options
  expect(option_menu).to_have_value("1")
  # switching option
  option_menu.select_option("3")
  expect(option_menu).to_have_value("3")

  # multiple options
  multi_option_menu = page.get_by_label("Example multiple select")
  multi_option_menu.select_option(["2", "4"])
  expect(multi_option_menu).to_have_values(["2", "4"])