from playwright.sync_api import Page, expect

def test_overlapped(page: Page):
  page.goto("http://uitestingplayground.com/overlapped")

  input = page.get_by_placeholder("Name")

  div = input.locator("..")
  div.hover()

  page.mouse.wheel(0, 200) # Page scrolling can cause flakiness and you have to do a manual wait afterwards

  data = "python"
  page.wait_for_selector("input[placeholder='Name']") # Fix flakiness that makes sure the input is editable after mouse scrolls
  input.fill(data)

  div.screenshot(path="test-overlapped.jpg")

  expect(input).to_have_value(data)