from playwright.sync_api import Route, Page, expect

# Modifying the response with the fulfill function
def on_route(route: Route):
  # Making up a response from scratch
  # route.fulfill(
  #   status=200,
  #   body="<html><body><h1>Custom Response!</h1></body></html>"
  # )

  # Getting the response object and manipulating it
  # by changing the text in the h1 tag
  response = route.fetch()
  body = response.text().replace(
    " enables reliable end-to-end testing for modern web apps.",
    " is an awesome framework for web automation!"
  )

  route.fulfill(
    response=response,
    body=body
  )


def test_docs_link(page: Page):
  page.route(
    "https://playwright.dev/python",
    on_route
  )

  page.goto("https://playwright.dev/python")
  page.pause()