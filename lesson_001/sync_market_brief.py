from agents import Runner
from agent import market_brief_agent

def main():
    result = Runner.run_sync(
        starting_agent=market_brief_agent,
        input=str(market_brief_agent.instructions)
    )

    print(result.final_output)


if __name__ == "__main__":
    main()
