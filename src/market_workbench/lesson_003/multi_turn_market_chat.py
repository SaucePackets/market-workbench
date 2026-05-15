import json
from agents import Runner
from dotenv import load_dotenv

from market_workbench.lesson_003.agent import market_agent


load_dotenv()

async def main():
    conversation_history = []
    first_message =  "Analyze NVDA"
    conversation_history.append({"role": "user", "content": first_message})
    result = await Runner.run(
        starting_agent=market_agent,
        input=conversation_history
    )

    conversation_history = result.to_input_list()

    second_message = "What about their competitors"
    conversation_history.append({"role": "user", "content": second_message})
    result = await Runner.run(
        starting_agent=market_agent,
        input=conversation_history
    )

    conversation_history = result.to_input_list()

    third_message = "Is NVDA a good investment"
    conversation_history.append({"role": "user", "content": third_message})
    result = await Runner.run(
        starting_agent=market_agent,
        input=conversation_history
    )

    conversation_history = result.to_input_list()

    print(json.dumps(conversation_history, indent=2))


    

