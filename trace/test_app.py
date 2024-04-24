import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
  # setup
  context.tracing.start(
    name="playwright",
    screenshots=True,
    snapshots=True,
    sources=True,
  )
  yield
  context.tracing.stop(path="trace.zip")

# VALUABLE Code
@pytest.fixture(autouse=True)
def trace_test_on_failure(request, browser_context: BrowserContext):
    # Start tracing before the test
    browser_context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    # Check if the test failed after the yield
    if request.node.rep_call.failed:
        # Stop tracing and save the trace if the test failed
        browser_context.tracing.stop(path="failure.zip")
    else:
        # Optionally, stop tracing without saving if the test passed
        browser_context.tracing.stop()


def test_page_has_get_started_link(page: Page):
  page.goto("https://playwright.dev/python")

  link = page.get_by_role("link", name="GET STARTED")
  link.click()

  assert page.url == DOCS_URL
