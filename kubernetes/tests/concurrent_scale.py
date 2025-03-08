import asyncio
import aiohttp

# Your Flask app URL
URL = "https://dog-web-app.wittycliff-7431e0fb.westeurope.azurecontainerapps.io/dog"

async def fetch_dog_image(session, request_id):
    """Fetch a random dog image from the Flask API."""
    async with session.get(URL) as response:
        data = await response.text()
        print(f"Request {request_id}: Status {response.status}")
        print(f"Response {request_id}: {data[:200]}...")  # Print first 200 chars to avoid long output

async def main():
    """Send 500 concurrent requests.
    This is to test Azure Container Instances' ability to scale up and handle concurrent requests.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_dog_image(session, i) for i in range(0, 500)]
        await asyncio.gather(*tasks)

# Run the async function
asyncio.run(main())
