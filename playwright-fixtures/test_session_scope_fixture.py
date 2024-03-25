from playwright.sync_api import Page, BrowserContext, Browser, BrowserType, Playwright, expect


def test_page_has_docs_link(playwright: Playwright, context: BrowserContext, browser: Browser, browser_type: BrowserType, is_firefox:bool, is_chromium: bool, is_webkit: bool):
  page = context.new_page()
  print(f"PLAYWRIGHT: {playwright}")
  print(f"CONTEXT: {context}")
  print(f"BROWSER: {browser}")
  print(f"BROWSER TYPE: {browser_type}")
  print(f"IS_FIREFOX: {is_firefox}")
  print(f"IS_CHROMIUM: {is_chromium}")
  print(f"IS_WEBKIT: {is_webkit}")

  page.goto("http://playwright.dev/python")

  docs_link = page.get_by_role("link", name="Docs")

  expect(docs_link).to_be_visible()


def test_get_started_visits_docs(page: Page):
  page.goto("http://playwright.dev/python")

  get_started_link = page.get_by_role(
    "link", name="GET STARTED"
  )
  get_started_link.click()

  expect(page).to_have_url(
    "http://playwright.dev/python/docs/intro"
  )