import asyncio
from dotenv import load_dotenv
from agents import Runner

from market_workbench.lesson_002.agent import market_brief_agent, portfolio_note_agent

load_dotenv()

async def main():
    brief_result = await Runner.run(
        starting_agent=market_brief_agent,
        input="Give me a cautious first-pass brief on MU.",
    )

    print(brief_result.input)
    print(brief_result.final_output)
    print(brief_result.last_agent.name)
    print(len(brief_result.new_items))

    portfolio_note_result = await Runner.run(
        starting_agent=portfolio_note_agent,
        input=brief_result.to_input_list() + [ {"role": "user", "content": "Write a portfolio journal note from this brief" } ]
    )

    print(portfolio_note_result.final_output)
    print(portfolio_note_result.last_agent.name)
    print(len(brief_result.new_items))

if __name__ == "__main__":
    asyncio.run(main())
