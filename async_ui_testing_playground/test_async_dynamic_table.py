import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_async_dynamic_table(page: Page):
    await page.goto("http://uitestingplayground.com/dynamictable")

    cpu_load_p = page.locator("p.bg-warning")
    percentage = await cpu_load_p.inner_text()
    percentage = percentage.split()[-1]

    column_headers = page.get_by_role("columnheader")
    cpu_column = None
    column_headers_count = await column_headers.count()

    for index in range(column_headers_count):
        column_header = column_headers.nth(index)
        column_header_text = await column_header.inner_text()

        if column_header_text == "CPU":
            cpu_column = index
            break

    assert cpu_column != None

    rowgroup = page.get_by_role("rowgroup").last
    chrome_row = rowgroup.get_by_role("row").filter(
        has_text="Chrome"
    )

    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    await expect(chrome_cpu).to_have_text(percentage)