import re
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
  page.goto("https://playwright.dev/python")

  docs_link = page.get_by_role("link", name="Docs")

  # to_have_class has to match all the classes in the class attribute
  expect(docs_link).to_have_class("navbar__item navbar__link")

  # testing if one class exists in the class attribute
  expect(docs_link).to_have_class(
    re.compile(r"navbar__link")
  )

  # test if the class attribute starts with navbar__item
  expect(docs_link).to_have_class(
    re.compile(r"^navbar__item")
  )

  # test the id attribute
  # expect(docs_link).to_have_id("playwright")

  expect(docs_link).to_have_attribute("href", "/python/docs/intro")