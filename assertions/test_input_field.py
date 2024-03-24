from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
  page.goto("https://playwright.dev/python")

  input = page.get_by_placeholder("Search docs")

  # input is hidden before button click
  expect(input).to_be_hidden()

  # search button
  search_btn = page.get_by_role("button", name="Search")
  # the key presses to pop open the search input dialog
  page.press("body", "Control+KeyK")
  
  # pressing Control+KeyK on the search_btn is not working
  # it is working in the Udemy tutorial
  # search_btn.press("Control+KeyK")
  
  # should pop the search menu
  expect(input).to_be_editable()
  expect(input).to_be_empty()

  # type some query in the input
  query = "assertions"
  input.fill(query)

  # check input value
  expect(input).to_have_value(query)