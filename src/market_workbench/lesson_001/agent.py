from agents import Agent

market_brief_agent = Agent (
    name="Market Brief Agent",
    instructions=(
        "You are a cautious market research assistant. "
        "Provide educational first-pass company briefs. "
        "If you lack current market data, say so clearly. "
        "Do not give personalized buy/sell advice."
    ),
    model="gpt-4.1",
)

market_brief_prompt = "Give me a cautious first-pass brief on MU."
