import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture(autouse=True)
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()

@pytest_asyncio.fixture(autouse=True)
async def context(browser):
    context = await browser.new_context(
        permissions=["clipboard-read", "clipboard-write"]
    )
    yield context
    await context.close()

@pytest_asyncio.fixture(autouse=True)
async def page(context):
    page = await context.new_page()
    page.set_default_timeout(120000) # Set timeout to 120 seconds
    yield page
    await page.close()