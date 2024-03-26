from playwright.sync_api import sync_playwright
from time import perf_counter


# This test should fail because this website is dependent on JavaScript
# It should timeout looking for td.film-title

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(
    headless=False, slow_mo=500
  )
  # Disables JavaScript on the browser.
  # Use this if you want to test your site works without JavaScript
  context = browser.new_context(java_script_enabled=False)

  page = context.new_page()
  page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

  link = page.get_by_role("link", name="2015")
  link.click()

  print("Loading oscars for 2015...")
  start = perf_counter()

  first_table_data = page.locator("td.film-title").first
  first_table_data.wait_for(timeout=4_000)

  time_taken = perf_counter() - start
  print(f"... movies are loaded, in {round(time_taken, 2)}s!")

  browser.close()