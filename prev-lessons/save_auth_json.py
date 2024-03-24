from playwright.sync_api import sync_playwright
import os

with sync_playwright() as playwright:
  browser = playwright.firefox.launch(headless=False)
  auth_json_path = "playwright/.auth/storage_state.json"

  # if storage_state.json exists, initiate the context with it for authentication
  if os.path.exists(auth_json_path):
    context = browser.new_context(
      storage_state=auth_json_path
    )
  else:
    context = browser.new_context()

  page = context.new_page()
  page.goto("https://gmail.com")

  # if you are signed because maybe the storage_state.json is timed out, pause the page
  # so you can manually reauthenticate to generate a new storage_state.json
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