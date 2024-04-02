import base64, pytest
from playwright.async_api import Page, expect, Error

@pytest.mark.asyncio
async def test_basic_auth(page: Page):
  """
  Write a test to log in with valid credentials and verify successful login by checking the presence of a specific element after login.
  """
  # The credentials
  username = "admin"
  password = "admin"
  # Encode the credentials
  credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

  await page.goto("https://the-internet.herokuapp.com/")

  await page.set_extra_http_headers({
    "Authorization": f"Basic {credentials}"
  })

  basic_auth_link = page.get_by_role("link", name="Basic Auth")
  await basic_auth_link.click()

  success_p = page.get_by_text("Congratulations! You must have the proper credentials.")
  await expect(success_p).to_be_visible()


@pytest.mark.asyncio
async def test_basic_auth_bad_credentials(page: Page):
  """
  Write a test to log in with invalid credentials and verify unsuccessful login
  by checking the error message.
  """
  # The bad credentials
  username = "badadmin"
  password = "badadmin"
  # Encode the credentials
  credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

  await page.goto("https://the-internet.herokuapp.com/")

  await page.set_extra_http_headers({
    "Authorization": f"Basic {credentials}"
  })

  with pytest.raises(Error):
    await page.goto("https://the-internet.herokuapp.com/basic_auth")