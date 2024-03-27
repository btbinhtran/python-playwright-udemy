from playwright.sync_api import sync_playwright, ViewportSize


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False, slow_mo=500)

  # Test on a Pixel 5 device
  # pixel_5_args = playwright.devices["Pixel 5"]
  # context = browser.new_context(**pixel_5_args)
  # context = browser.new_context(
  #   viewport={
  #     "width": 300,
  #     "height": 500,
  #   }
  # )

  # Changing the browser color scheme to "dark"
  context = browser.new_context(
    color_scheme="dark",
    # Some options you can set on a context
    # permissions=
    # geolocation=
    # locale=
  )

  page = context.new_page()
  page.goto("https://playwright.dev/python")

  link = page.get_by_role("link", name="GET STARTED")
  link.click()

  # Good for testing after the viewport has changed after some action
  page.set_viewport_size({
    "width": 1000,
    "height": 1000,
  })