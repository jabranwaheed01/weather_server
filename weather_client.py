import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["weather_server.py"],
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("\nAvailable Tools:")

            for tool in tools.tools:
                print("-", tool.name)

                print("\nCalling get_forecast...")

                result = await session.call_tool(
                    "get_forecast",
                    arguments={
                        "latitude": 29.7604,
                        "longitude": -95.3698
                    }
                )

                print("\nWeather Forecast:")
                print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())