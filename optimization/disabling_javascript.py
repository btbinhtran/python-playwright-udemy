import os, time, pytest
from playwright.sync_api import *


@pytest.fixture
def browser_context_args():
  return {
    "java_script_enabled": False
  }


NOT_ALLOWED_RESOURCES = (
  "image", "font", "stylesheet", "media"
)


def on_route(route: Route):
  if route.request.resource_type in NOT_ALLOWED_RESOURCES:
    route.abort()
  else:
    route.continue_()


def check_mail(playwright: Playwright):
  browser = playwright.firefox.launch()
  auth_json_path = "playwright/.auth/storage_state.json"

  if os.path.exists(auth_json_path):
    context = browser.new_context(
      storage_state=auth_json_path
    )
  else:
    context = browser.new_context()

  page = context.new_page()
  # Commenting out the line below should make the test run slower with
  # the overhead of loading images, fonts, stylesheets, and media
  page.route("**", on_route)
  page.goto("https://gmail.com")

  if page.get_by_text("Signed out").is_visible() or page.get_by_text("Sign in").first.is_visible():
    page.pause()
    context.storage_state(
      path=auth_json_path
    )

  new_emails = []
  emails = page.locator("div.UI table tr")
  
  for email in emails.all():
    is_new_email = email.locator(
      "td li[data-tooltip='Mark as read']"
    ).count() == 1

    if is_new_email:
      sender = email.locator("td span[email]:visible").inner_text()
      title = email.locator("td span[data-thread-id]:visible").inner_text()

      new_emails.append(
        [sender, title]
      )

  if len(new_emails) == 0:
    print("No new emails 📥!")
  else:
    print(f"{len(new_emails)} new emails 🥊!")
    print("-"*30)

    for new_email in new_emails:
      print(new_email[0] + ":", new_email[1])
      print("-"*30)


  context.close()


with sync_playwright() as playwright:
  start = time.perf_counter()

  check_mail(playwright)

  time_taken = time.perf_counter() - start
  
  print(f"Time taken {round(time_taken, 2)}s")