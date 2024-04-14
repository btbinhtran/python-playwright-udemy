import pytest, pytest_asyncio
from playwright.async_api import Page, expect


@pytest_asyncio.fixture(autouse=True)
async def visit_test_page(page: Page):
  await page.goto("http://uitestingplayground.com/sampleapp", wait_until="networkidle")


@pytest.mark.asyncio
async def test_async_successful_login(page: Page):
  username = "dan"
  password = "pwd"

  username_input = page.get_by_placeholder("User Name")
  password_input = page.get_by_placeholder("********")
  login_btn = page.get_by_role("button", name="Log In")

  await username_input.fill(username)
  await password_input.fill(password)

  await login_btn.click()

  label = page.locator("label#loginstatus")
  await expect(label).to_have_text(f"Welcome, {username}!")


@pytest.mark.asyncio
async def test_async_failed_login(page: Page):
  username = "dan"
  password = "badpasswordfriend"

  username_input = page.get_by_placeholder("User Name")
  password_input = page.get_by_placeholder("********")
  login_btn = page.get_by_role("button", name="Log In")

  await username_input.fill(username)
  await password_input.fill(password)

  await login_btn.click()

  label = page.locator("label#loginstatus")

  await expect(label).to_have_text("Invalid username/password")

@pytest.mark.asyncio
async def test_async_logout(page: Page):
  username = "dan"
  password = "pwd"

  username_input = page.get_by_placeholder("User Name")
  password_input = page.get_by_placeholder("********")
  login_btn = page.get_by_role("button", name="Log In")

  await username_input.fill(username)
  await password_input.fill(password)

  await login_btn.click()

  label = page.locator("label#loginstatus")
  await expect(label).to_have_text(f"Welcome, {username}!")

  logout_btn = page.get_by_role("button", name="Log Out")
  await logout_btn.click()
  await expect(label).to_have_text("User logged out.")