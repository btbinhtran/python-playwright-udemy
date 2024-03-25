from playwright.sync_api import Route, Page, expect

# Used to abort a request
# def on_route(route: Route):
#   print("Request aborted:", route.request)
#   route.abort()

# Used to abort all images
def on_route(route: Route):
  if route.request.resource_type == "image":
    route.abort()
  else:
    route.continue_()


def test_docs_link(page: Page):
  # Abort a specific route
  # In this case, abort a svg image request
  # page.route(
  #   "https://playwright.dev/python/img/playwright-logo.svg",
  #   on_route
  # )

  # Abort every png image request
  # page.route(
  #   "**/*.png",
  #   on_route
  # )

  # Selects every url
  page.route(
      "**",
      on_route
  )

  page.goto("https://playwright.dev/python")

  page.screenshot(path="playwright.jpg", full_page=True)