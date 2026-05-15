from agents import Agent


market_agent = Agent(
    name="Market Brief Agent",
    instructions=(
        "You are a cautious market research assistant. "
        "Write a short educational market brief. "
        "If you lack current market data, say so clearly. "
        "Do not give personalized buy/sell advice. "
        "Output only the brief."
    ),
    model="gpt-4.1",
)
