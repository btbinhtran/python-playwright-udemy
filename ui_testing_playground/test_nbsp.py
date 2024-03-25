from playwright.sync_api import Page, expect

def test_nbsp(page: Page):
  page.goto("http://uitestingplayground.com/nbsp")

  # Look on https://en.wikipedia.org/wiki/List_of_Unicode_characters
  # to figure out which unicode character matches to the HTML character
  page.locator("//button[text()='My\u00a0Button']").click(timeout=2000)