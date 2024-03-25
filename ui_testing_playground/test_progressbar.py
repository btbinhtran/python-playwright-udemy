from playwright.sync_api import Page, expect

def test_progressbar(page: Page):
  page.goto("http://uitestingplayground.com/progressbar")

  progressbar = page.get_by_role("progressbar")

  start_btn = page.get_by_role("button", name="Start")
  stop_btn = page.get_by_role("button", name="Stop")

  start_btn.click()

  while True:
    valuenow = int(progressbar.get_attribute("aria-valuenow"))

    if valuenow >= 75:
      break
    else:
      print(f"Percent: {valuenow}%")

  stop_btn.click()

  assert valuenow >= 75