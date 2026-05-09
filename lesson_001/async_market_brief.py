
import asyncio
from agents import Runner

from lesson_001.agent import market_brief_agent


async def main():
    result = await Runner.run(
        starting_agent=market_brief_agent,
        input=str(market_brief_agent.instructions)
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main=main())
