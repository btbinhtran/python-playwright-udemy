import pytest
import pytest_asyncio
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
async def test_async_class_attribute(page):
    await page.goto("http://uitestingplayground.com/classattr")
    
    primary_btn = page.locator("button.btn-primary")

    await expect(primary_btn).to_be_visible()

    await primary_btn.click()
