from dotenv import load_dotenv
import asyncio
from agents import Runner

from lesson_001.agent import market_brief_agent, market_brief_prompt

load_dotenv()


async def main():
    result = await Runner.run(
        starting_agent=market_brief_agent,
        input=market_brief_prompt
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
