from playwright.sync_api import Page, expect

def test_contains_text(page: Page):
  page.goto("http://uitestingplayground.com/verifytext")

  text = page.locator("div.bg-primary").get_by_text("Welcome")

  expect(text).to_have_text("Welcome UserName!")