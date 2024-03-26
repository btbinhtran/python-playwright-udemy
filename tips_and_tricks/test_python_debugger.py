from playwright.sync_api import Page, expect


def test_page_has_get_started_link(page: Page):
  page.goto("https://playwright.dev/python")

  docs_link = page.get_by_role("link", name="GET STARTED")

  expect(docs_link).to_be_visible()


def test_page_visits_docs(page: Page):
  page.goto("https://playwright.dev/python")

  link = page.get_by_role("link", name="GET STARTED")

  breakpoint()

  link.click()

  expect(page).to_have_url(
    "https://playwright.dev/python/docs/intro"
  )