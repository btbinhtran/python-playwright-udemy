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
* `pytest --flake-finder --flake-runs=20` - Find flaky tests by running multiple times
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

# BDD

## Prompt to Prime AI to help generate Gherkin Scenarios
```Text
Act as a quality analyst who is highly experienced in behavioral driven development and developing well-constructed Gherkin Scenarios from supplied requirements. 
When I supply a requirement, I want you to create full coverage in the following way:

1. Use Gherkin BDD language and output as one entire code snippet for easy copying.
2. Provide positive and negative scenarios. 
3. Ensure all common steps you create are added as a Gherkin ‘Background’.
4. Ensure ‘Background’ is provided only once and is placed after the user story and before the scenarios. 
5. Ensure all variables used are created as a Gherkin ‘Scenario Outline’.
6. Ensure variables are added to a Gherkin ‘Examples’ table appropriately.
7. Include feature level tags and scenario level tags e.g., @valid, @invalid, @feature-example, @smoke-test, @regression-test.
8. Provide feature and user story.
9. Afterwards, suggest an appropriate name for the *.feature file and explain your working.
10. Do not assume any output like error messages or variables not part of the requirements. 

Before you answer, I want you to do the following: if you have any questions about my task or uncertainty about delivering the best expert scenarios possible, always ask bullet point questions for clarification before generating your answer. 

Is that understood and are you ready for the requirements?
```

## Gherkin's Golden Rule
> [!IMPORTANT]
> Treat other readers as you would want to be treated:
>
> Write feature files so that everyone can intuitively understand them.

### Gherkin Scenario recommendations
* Be declarative
* Follow strict step type order
  - Given -> When -> Then
* Write concise scenarios
  - Single-digit length
* Write steps chronologically
  - So they can be automated
* Avoid low-level interactions
* Respect step types

### Good example
```Gherkin
Scenario: Add shoes to the shopping cart
  Given the ShoeStore home page is displayed
  When the shopper searches for "red pumps"
  And the shopper adds the first result to the cart
  Then the cart has one pair of "red pumps"
```

## The Cardinal Rule of BDD
> [!IMPORTANT]
> One scenario should cover exactly one individual, independent behavior.
>
> When focusing on one behavior at a time:

|  |  |
| --- | --- |
| **Collaboration** | More focus + less confusion |
| **Automation** | Each test failure points to a unique problem |
| **Efficiency** | Less complex work => faster cycle times |
| **Traceability** | One behavior -> one example -> one scenario -> one test -> one result |
| **Accountability** | Teams cannot hide or avoid behaviors |

### 2 Behaviors in 1 Scenario

**BAD**
```Gherkin
Feature: Product Searching
  As a shopper,
  I want to search for new items,
  so that I can buy what I want.

  Scenario: Simple product search
    Given the ShoeStore home page is displayed
    When the search phrase "red pumps" is entered # 1st Scenario
    Then results for "red pumps" are shown        #
    When the user searches for images from the results page # 2nd Scenario
    Then image results for "red pumps" are shown            #
```

**GOOD:** Split into 2 Scenarios
```Gherkin
Feature: Product Searching

  Scenario: Simple Web search
    Given the ShoeStore home page is displayed
    When the search phrase "red pumps" is entered
    Then results for "red pumps" are shown

  Scenario: Simple Web image search
    Given ShoeStore search results for "red pumps" are displayed
    When the user searches for images from the results page
    Then image results for "red pumps" are shown
```

## The Unique Example Rule
> [!IMPORTANT]
> Don't include unnecessary examples.
> Focus on unique input *equivalence* classes.

**BAD:** Example Overload
```Gherkin
Feature: Product Searching

  Scenario Outline: Simple product search
    Given the ShoeStore home page is displayed
    When the search phrase "<phrase>" is entered
    Then results for "<phrase>" are shown

    Examples: Shoes
      | phrase        | # The only example you need. Remove the ones below.
      | red pumps     |
      | sneakers      |
      | sandals       |
      | flip flops    |
      | flats         |
      | slippers      |
      | running shoes |
```

## The Fourth Amigo Rule
> [!IMPORTANT]
> Pretend that your high school English teacher is the "Fourth Amigo" reading your Gherkin.

### Why Proper English Matters
Behavior scenarios are meant to be *readable* and *expressive*. Steps are also meant to be *reusable*.

Poor grammar, misspellings, and inconsistent phrasing can ruin the benefits of behavior specification.
Scenarios can become confusing. Improper steps could be used.

### Point of View
> [!IMPORTANT]
> Use Third-Person

```Gherkin
Given the ShoeStore home page is displayed
When the user searches for "red pumps"
Then links related to "red pumps" are shown on the results page
```

### Subject-Predicate Phrases
> [!IMPORTANT]
> All steps should use **subject-predicate phrases**.

Subject-predicate phrases capture the appropriate context for steps.

Scenarios also provide context.
However, when steps are reused elsewhere, the scenario is not there to provide the context.

Thus, **each step must make sense in its own right.**

**GOOD**
```Gherkin
Scenario: Simple product search
  Given the ShoeStore home page is displayed
  When the search phrase "sneakers" is entered
  Then the results page shows links related to "sneakers"
  And the results page shows image links for "sneakers"
  And the results page shows video llinks for "sneakers"
```