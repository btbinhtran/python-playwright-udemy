import pytest
from playwright.async_api import Page, expect, TimeoutError

@pytest.mark.asyncio
async def test_async_visibility(page: Page):
  await page.goto("http://uitestingplayground.com/visibility")

  hide_btn = page.get_by_role("button", name="Hide")
  removed_btn = page.get_by_role("button", name="Removed")
  zero_width_btn = page.get_by_role("button", name="Zero Width")
  overlapped_btn = page.get_by_role("button", name="Overlapped")
  opacity_0_btn = page.get_by_role("button", name="Opacity 0")
  visibility_hidden_btn = page.get_by_role("button", name="Visibility Hidden")
  display_none_btn = page.get_by_role("button", name="Display None")
  offscreen_btn = page.get_by_role("button", name="Offscreen")

  await hide_btn.click()

  await expect(removed_btn).to_be_hidden()

  await expect(zero_width_btn).to_have_css("width", "0px")

  with pytest.raises(TimeoutError):
    await overlapped_btn.click(timeout=2000)

  await expect(opacity_0_btn).to_have_css("opacity", "0")

  await expect(visibility_hidden_btn).to_be_hidden()

  await expect(display_none_btn).to_be_hidden()

  await expect(offscreen_btn).not_to_be_in_viewport()