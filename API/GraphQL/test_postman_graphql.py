from playwright.async_api import async_playwright, APIRequestContext, expect, Playwright
import pytest, pytest_asyncio, json


@pytest_asyncio.fixture
async def api_context():
  async with async_playwright() as p:
    api_context = await p.request.new_context(
      base_url="https://graphql.postman-echo.com/graphql",
      extra_http_headers={
        'Accept': '*/*',
        'Content-Type': 'application/json'
      }
    )
    yield api_context
    await api_context.dispose()


@pytest.mark.asyncio
async def test_graphql_echo(api_context: APIRequestContext):
  # Simple query to test fetching a hello message
  query = """
  query Hello {
    hello(person: { name: "Binh" })
  }
  """

  # Send the GraphQL request using api_context
  response = await api_context.post(
    "", # I put the graphql endpoint in the base_url but you still need to pass a blank url string
    data=json.dumps({"query": query})
  )

  status_code = response.status
  assert status_code == 200, f"Unexpected status code: {status_code}"

  data = await response.json()
  assert "data" in data
  assert data["data"]["hello"] == "Hello Binh"


@pytest.mark.asyncio
async def test_graphql_bad_query(api_context: APIRequestContext):
  # Simple query to test fetching a hello message
  query = """
  query Hello {
    hello
  """

  # Send the GraphQL request using api_context
  response = await api_context.post(
    "", # I put the graphql endpoint in the base_url but you still need to pass a blank url string
    data=json.dumps({"query": query})
  )

  status_code = response.status
  assert status_code == 200, f"Unexpected status code: {status_code}"

  data = await response.json()

  assert "errors" in data
  assert isinstance(data["errors"], list)
  assert len(data["errors"]) == 1
  assert "message" in data["errors"][0]
  assert "locations" in data["errors"][0]
  assert data["errors"][0]["message"] == 'Syntax Error: Expected Name, found <EOF>.'
  assert isinstance(data["errors"][0]["locations"], list)
  assert len(data["errors"][0]["locations"]) == 1
  assert "line" in data["errors"][0]["locations"][0]
  assert "column" in data["errors"][0]["locations"][0]
  assert data["errors"][0]["locations"][0]["line"] == 4
  assert data["errors"][0]["locations"][0]["column"] == 3


@pytest.mark.asyncio
async def test_graphql_request(api_context: APIRequestContext):
  # Simple query to test fetching a hello message
  query = """
  query Request {
      request {
          headers
      }
  }
  """

  # Send the GraphQL request using api_context
  response = await api_context.post(
    "", # I put the graphql endpoint in the base_url but you still need to pass a blank url string
    data=json.dumps({"query": query})
  )

  status_code = response.status
  assert status_code == 200, f"Unexpected status code: {status_code}"

  data = await response.json()

  assert "data" in data
  assert "request" in data["data"]
  assert "headers" in data["data"]["request"]

  expected_header_keys = [
    "connection",
    "accept",
    "content-length",
    "content-type",
    "host",
    "user-agent",
    "x-amzn-trace-id",
    "x-forwarded-for",
    "x-forwarded-port",
    "x-forwarded-proto"
  ]

  # Assert all header values
  expected_headers = {
    "connection": "keep-alive",
    "accept": "*/*",
    "content-type": "application/json",
    "host": "graphql.postman-echo.com",   
    "x-forwarded-for": "99.105.214.91",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https"
  }

  # Assert header keys exist
  for header_key in expected_header_keys:
    assert header_key in data["data"]["request"]["headers"], f"Header {header_key} is not found in response."

  # Assert all header values
  for header, expected_value in expected_headers.items():
    assert data["data"]["request"]["headers"][header] == expected_value, f"Unexpected value for header '{header}'"

@pytest.mark.asyncio
async def test_graphql_createPerson_mutation(api_context: APIRequestContext):
  """
  Expected Response:
  {
      "data": {
          "createPerson": {
              "id": "74", # This can be different
              "name": "Joe Dirt",
              "age": 30
          }
      }
  }
  """
  # Simple query to test fetching a hello message
  # Define the GraphQL mutation
  mutation = """
  mutation CreatePerson {
      createPerson(person: { name: "John Doe", age: 30}) {
        id
        name
        age
      }
  }
  """

  response = await api_context.post("", data=json.dumps({"query": mutation}))

  await expect(response).to_be_ok()

  # Parse the JSON response
  response_data = await response.json()
  print(response_data)

  # Assert presence of "data" key
  assert "data" in response_data, "Missing 'data' key in response"
  assert "createPerson" in response_data["data"]
  assert "id" in response_data["data"]["createPerson"]
  assert response_data["data"]["createPerson"]["name"] == "John Doe"
  assert response_data["data"]["createPerson"]["age"] == 30


@pytest.mark.asyncio
async def test_graphql_greetings_subscription(api_context: APIRequestContext):
  # Define the GraphQL subscription query
  subscription_query = """
  subscription Greetings {
    greetings
  }
  """

  response = await api_context.post("", data=json.dumps({"query": subscription_query}))
  messages = (await response.text()).strip().split('\n\n')

  # Parse each message as JSON and store in a list
  parsed_messages = []
  for message in messages:
    # Remove the "data: " prefix (if present)
    if message.startswith('data: '):
      message = message[6:]
    parsed_messages.append(json.loads(message))

  # Expecting parsed_messages to look like:
  # [
  #   {
  #     "data": {
  #       "greetings": "Hi"
  #     }
  #   },
  #   {
  #     "data": {
  #       "greetings": "Bonjour"
  #     }
  #   },
  #   {
  #     "data": {
  #       "greetings": "Hola"
  #     }
  #   },
  #   {
  #     "data": {
  #       "greetings": "Ciao"
  #     }
  #   },
  #   {
  #     "data": {
  #       "greetings": "Zdravo"
  #     }
  #   }
  # ]
  

  expected_greetings = [
    "Hi",
    "Bonjour",
    "Hola",
    "Ciao",
    "Zdravo"
  ]
  assert len(parsed_messages) == 5
  for data, greeting in zip(parsed_messages, expected_greetings):
    assert "data" in data
    assert "greetings" in data["data"]
    assert data["data"]["greetings"] == greeting