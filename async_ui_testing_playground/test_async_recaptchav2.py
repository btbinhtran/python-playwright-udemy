# This is an example of using a reCAPTCHAv2 Solving Service.
# This is not the best way to test a web form that has reCAPTCHA.
# * You would want to have a test mode that doesn't show the reCAPTCHA.
# * You can try to mock the response from the server to bypass the actual
#   reCAPTCHA solving step.

import pytest
from playwright.async_api import Page, expect
from playwright_recaptcha import (
    CapSolverError,
    RecaptchaNotFoundError,
    RecaptchaRateLimitError,
    recaptchav2,
)

@pytest.mark.asyncio
@pytest.mark.xfail(raises=RecaptchaRateLimitError)
async def test_async_solver_with_normal_recaptcha(page: Page):
  """Test the solver with a normal reCAPTCHA."""
  await page.goto("https://www.google.com/recaptcha/api2/demo")
  async with recaptchav2.AsyncSolver(page) as solver:
    await solver.solve_recaptcha(wait=True)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=(RecaptchaNotFoundError, RecaptchaRateLimitError))
async def test_async_solver_with_hidden_recaptcha(page: Page):
  """Test the solver with a hidden reCAPTCHA"""
  await page.goto("https://www.google.com/recaptcha/api2/demo?invisible=true")
  submit_btn = page.get_by_role("button", name="Submit")
  await submit_btn.click()

  async with recaptchav2.AsyncSolver(page) as solver:
    await solver.solve_recaptcha(wait=True)


@pytest.mark.asyncio
@pytest.mark.xfail(raises=CapSolverError)
async def test_async_solver_with_image_challenge(page: Page):
  await page.goto("https://www.google.com/recaptcha/api2/demo")

  async with recaptchav2.AsyncSolver(page) as solver:
    await solver.solve_recaptcha(wait=True, image_challenge=True)


@pytest.mark.asyncio
async def test_async_recaptcha_not_found_error(page: Page):
  await page.goto("https://www.google.com/")

  with pytest.raises(RecaptchaNotFoundError):
    async with recaptchav2.AsyncSolver(page) as solver:
      await solver.solve_recaptcha()