# Locators from most to least preferred
1. **Role and Text:** `page.get_by_role("button", name="Submit")`
2. **Test ID:** `page.get_by_test_id("add-to-cart-button)`
3. **CSS Selector:** `page.locator("button.myId")`
4. **XPATH as a Last Resort:** `page.locator('//button[@text()='Click me']')`

# Install necessary Pip packages
* `pip install -r requirements.txt`

# Open URL to Debug and Record Your Scripts
* `playwright codegen test_url`

# pytest CLI Arguments
* `pytest --headed` - Browser is visible
* `pytest --slowmo=400` - Slow interactions to 400 milliseconds
* `pytest --browser=firefox|webkit` - Select browser to run on
* `pytest --device="Pixel 5"` - Select device to run on
* `pytest --tracing on|off|retain-on-failure` - Toggle tracing
* `pytest -n auto` - Run tests on the max number of threads allowed on your system (# CPUs * # of threads per CPU)
* `pytest --video on` - Record the test as a video
* `pytest --screenshot on|only-on-failure` - Take screenshot at the end of the test execution, when test finished
* `pytest -k test_page_visits_docs` - Run test by it's specific function name

# Playwright in Python REPL
## Setting up the page to test out locators and selectors
* `from playwright.sync_api import sync_playwright`
* `playwright = sync_playwright().start()`
* `browser = playwright.chromium.launch(headless=False, slow_mo=100)`
* `page = browser.new_page()`
* `page.goto('https://playwright.dev/python')`
* `btn = page.get_by_role("link", name="GET STARTED")`
* `btn.highlight()` - This visibly highlights the locator on the browser

## Cleaning up the Python REPL session
* `browser.close()`
* `playwright.stop()`
* `exit()`

# Must see repositories
* [Repo that shows how to setup pytest-bdd steps with async Playwright](https://github.com/btbinhtran/pytest_bdd_tau)
* [AutomationPanda: playwright-python-tutorial](https://github.com/AutomationPanda/playwright-python-tutorial)
* [AutomationPanda: awesome-web-testing-playwright](https://github.com/AutomationPanda/awesome-web-testing-playwright)
* [AutomationPanda: Screenplay Pattern library using Python](https://github.com/AutomationPanda/screenplay)
* [AutomationPanda: How to use Python screenplay library with Selenium](https://github.com/AutomationPanda/selenium-screenplay-python)

# Other resources
* [Test Automation University: Behavior Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
* [BrowserStack: Playwright Python Tutorial](https://www.browserstack.com/guide/playwright-python-tutorial)
* [Udemy: Playwright Python and Pytest for Web Automation Testing](https://www.udemy.com/course/playwright-python-pytest)
* [pytest-asyncio docs](https://pytest-asyncio.readthedocs.io/en/latest/)
* [Real Python: Concurrency With the asyncio Module](https://realpython.com/courses/python-3-concurrency-asyncio-module/)