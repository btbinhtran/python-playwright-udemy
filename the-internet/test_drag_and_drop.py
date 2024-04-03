import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_drag_and_drop(page: Page):
  """
  Navigates to the webpage.
  Verifies the initial content of the draggable element (e.g., "Draggable A") and the droppable element (e.g., "Drop here").
  Performs a drag-and-drop interaction by moving the draggable element onto the droppable element.
  Verifies that the content of the elements is swapped after the drag-and-drop (e.g., the draggable element now has the content "Drop here" and the droppable element has the content "Draggable A").
  """
  await page.goto("https://the-internet.herokuapp.com/drag_and_drop")

  columns = page.locator("div#columns div.column")

  await expect(columns.first).to_have_text("A")
  await expect(columns.last).to_have_text("B")

  await page.drag_and_drop("div#column-a", "div#column-b")

  await expect(columns.first).to_have_text("B")
  await expect(columns.last).to_have_text("A")