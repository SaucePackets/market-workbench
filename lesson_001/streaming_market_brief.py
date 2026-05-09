
import asyncio
from agents import Runner, result

from lesson_001.agent import market_brief_agent


async def main():
    result = Runner.run_streamed(
        starting_agent=market_brief_agent,
        input=str(market_brief_agent.instructions)
    )

    async for r in result.stream_events():
        print(r)

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main=main())
