# This is an example of using a RECAPTCHAv2 Solving Service.
# This is not the best way to test a web form that has RECAPTCHA.
# * You would want to have a test mode that doesn't show the RECAPTCHA.
# * You can try to mock the response from the server to bypass the actual
#   RECAPTCHA solving step.

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
async def test_async_recaptchav2(page: Page):
  """Test the solver with a normal reCAPTCHA."""
  await page.goto("https://www.google.com/recaptcha/api2/demo")
  async with recaptchav2.AsyncSolver(page) as solver:
    await solver.solve_recaptcha(wait=True)