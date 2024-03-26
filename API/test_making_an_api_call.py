import json
from playwright.sync_api import *


def test_users_api(page: Page):
  response = page.goto("https://dummyjson.com/users/1")

  # The 2 lines below do the same thing
  # The 2nd line which is uncommented is the preferred way
  # user_data = json.loads(response.body)
  user_data = response.json()

  assert "firstName" in user_data
  assert "lastName" in user_data

  assert user_data["firstName"] == "Terry"
  assert user_data["lastName"] == "Medhurst"