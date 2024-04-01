import pytest, pytest_asyncio
from playwright.async_api import async_playwright, expect

@pytest_asyncio.fixture(autouse=True)
async def browser():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    yield browser
    await browser.close()

@pytest_asyncio.fixture(autouse=True)
async def context(browser):
  context = await browser.new_context()
  yield context
  await context.close()

@pytest_asyncio.fixture(autouse=True)
async def page(context):
  page = await context.new_page()
  yield page
  await page.close()


@pytest.mark.asyncio
async def test_dynamic_id(page):
  await page.goto("http://uitestingplayground.com/dynamicid")

  button = page.get_by_role(
    "button", name="Button with Dynamic ID"
  )
  await expect(button).to_be_visible()
  await button.click()