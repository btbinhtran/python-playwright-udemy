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