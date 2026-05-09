from dotenv import load_dotenv
from agents import Runner

from lesson_001.agent import market_brief_agent, market_brief_prompt

load_dotenv()

def main():
    result = Runner.run_sync(
        starting_agent=market_brief_agent,
        input=market_brief_prompt
    )

    print(result.final_output)


if __name__ == "__main__":
    main()
