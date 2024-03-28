from playwright.sync_api import sync_playwright


# custom page load event listener function
def on_load(page):
  print("Page loaded:", page)

# custom page domcontentloaded event listener function
def on_domcontentloaded(page):
  print("Page domcontentloaded:", page)


# custom page close event listener function
def on_close(page):
  print("Page close:", page)


def on_response(response):
  print("Response:", response)


def on_request(request):
  print("Request sent:", request)

# handle choosing opening a file dialog
def on_filechooser(file_chooser):
  print("File chooser opened")
  file_chooser.set_files("file.txt")


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(
    headless=False, slow_mo=500
  )
  page = browser.new_page()
  # This will always listen to the event
  page.on("load", on_load)

  # This will only listen to the event once
  # page.once("load", on_load)

  page.on("domcontentloaded", on_domcontentloaded)

  page.on("close", on_close)

  page.on("response", on_response)

  page.on("request", on_request)

  page.on("filechooser", on_filechooser)


  page.goto("https://bootswatch.com/default")

  file_input = page.get_by_label("Default file input example")
  file_input.click()

  # Always remove event listeners when you are cleaning up
  page.remove_listener("load", on_load)

  page.remove_listener("domcontentloaded", on_domcontentloaded)

  page.remove_listener("close", on_close)

  page.remove_listener("response", on_response)

  page.remove_listener("request", on_request)

  page.remove_listener("filechooser", on_filechooser)

  browser.close()