import pytest
from playwright.sync_api import *


@pytest.fixture
def api_context(playwright: Playwright):
  api_context = playwright.request.new_context(
    base_url="https://dummyjson.com",
    extra_http_headers={'Content-Type': 'application/json'},
  )
  yield api_context
  api_context.dispose()


def test_create_user(api_context: APIRequestContext):
  # This does the same as api_context.post()
  # api_context.fetch(
  #   "users/add",
  #   method="POST",
  #   headers={'Content-Type': 'application/json'},
  #   data={
  #     "firstName": "Damien",
  #     "lastName": "Smith",
  #     "age": 27
  #   }
  # )
  
  response = api_context.post(
    "users/add",
    data={
      "firstName": "Damien",
      "lastName": "Smith",
      "age": 27
    }
  )
  user_data = response.json()

  print(f"\n{user_data}")

  assert user_data["id"] == 101
  assert user_data["firstName"] == "Damien"

  response = api_context.delete(f"users/{user_data['id']}")


def test_update_user(api_context: APIRequestContext):

  print(api_context.get("users/1").json()["lastName"])

  response = api_context.put(
    "users/1",
    data={
      "lastName": "Smith",
      "age": 20,
    }
  )
  user_data = response.json()

  print(user_data)

  assert user_data["lastName"] == "Smith"
  assert user_data["age"] == 20


def test_delete_user(api_context: APIRequestContext):
  user_id = 1
  response = api_context.delete(f"users/{user_id}")
  deleted_user_data = response.json()

  assert deleted_user_data["id"] == user_id
  assert deleted_user_data["isDeleted"] == True
  assert "deletedOn" in deleted_user_data