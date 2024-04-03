from playwright.async_api import async_playwright, APIRequestContext, Playwright
import pytest, pytest_asyncio, json


@pytest_asyncio.fixture
async def api_context():
  async with async_playwright() as p:
    api_context = await p.request.new_context(
      base_url="https://graphql.postman-echo.com/graphql",
      extra_http_headers={'Content-Type': 'application/json'}
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
  print("DATADATADATA")
  print(data)
  assert data["data"]["hello"] == "Hello Binh"