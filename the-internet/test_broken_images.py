import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_broken_images(page: Page):
  """
  Verify that all images displayed on the webpage are valid and not broken.
  """
  await page.goto("https://the-internet.herokuapp.com/broken_images")

  images = page.locator("img")
  image_count = await images.count()

  for index in range(image_count):
    image = images.nth(index)
    image_url = await image.get_attribute("src")

    try:
      response = await page.goto(image_url, wait_until="networkidle")  
    except Exception as e:
      assert False, f"'{image_url}' is not a displayable image"