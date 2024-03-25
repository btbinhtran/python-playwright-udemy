from playwright.sync_api import Page, expect

def test_load_delay(page: Page):
  page.goto("http://uitestingplayground.com/clientdelay")

  btn = page.get_by_role("button", name="Button Triggering Client Side Logic")
  btn.click()

  paragraph = page.locator("p.bg-success")
  paragraph.wait_for()

  paragraph.click()
  expect(paragraph).to_have_text("Data calculated on the client side.")