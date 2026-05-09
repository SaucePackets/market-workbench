from dotenv import load_dotenv
import asyncio
from agents import Runner

from market_workbench.lesson_001.agent import market_brief_agent, market_brief_prompt

load_dotenv()

async def main():
    result = Runner.run_streamed(
        starting_agent=market_brief_agent,
        input=market_brief_prompt
    )

    async for r in result.stream_events():
        print(r)

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
