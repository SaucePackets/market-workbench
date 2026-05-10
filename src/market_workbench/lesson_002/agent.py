from agents import Agent

market_brief_agent = Agent (
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

portfolio_note_agent = Agent(
    name="Portfolio Note Agent",
    instructions=(
        "You are a portfolio journal assistant. "
        "Given a market brief, write a concise portfolio journal note."
        "Include a thesis summary, caveats, follow-up questions, "
        "and the exact line: No trade action taken. "
        "Do not recommend buying or selling."
    ),
    model="gpt-4.1",
)
