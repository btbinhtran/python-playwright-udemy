# This is an example of using a reCAPTCHAv3 Solving Service.
# This is not the best way to test a web form that has reCAPTCHA.
# * You would want to have a test mode that doesn't show the reCAPTCHA.
# * You can try to mock the response from the server to bypass the actual
#   reCAPTCHA solving step.
import pytest
from playwright.async_api import async_playwright, Page
from playwright_recaptcha import RecaptchaTimeoutError, recaptchav3


@pytest.mark.asyncio
async def test_async_solver_with_normal_browser(page: Page):
  """Test the solver with a normal browser"""
  await page.goto("https://antcpt.com/score_detector/")

  async with recaptchav3.AsyncSolver(page) as solver:
    await solver.solve_recaptcha()


@pytest.mark.asyncio
async def test_async_recaptcha_not_found_error(page: Page):
  """Test the solver with a page that does not have a reCAPTCHA."""
  await page.goto("https://www.google.com/")

  with pytest.raises(RecaptchaTimeoutError):
    async with recaptchav3.AsyncSolver(page, timeout=10) as solver:
      await solver.solve_recaptcha()