# Lesson 001 — OpenAI Agents SDK Basics

## Course concept

Create an `Agent`, then execute it with `Runner` using sync, async, or streaming mode.

## Project translation

Build a `Market Brief Agent`.

It should:

- accept a ticker prompt like `Give me a cautious first-pass brief on NVDA`
- explain that it does not have live market data yet
- avoid buy/sell recommendations
- produce a structured first-pass brief

## Your implementation task

Create three scripts under `src/market_workbench/lesson_001/`:

- `sync_market_brief.py`
- `async_market_brief.py`
- `streaming_market_brief.py`

Each should use the same agent definition:

```python
Agent(
    name="Market Brief Agent",
    instructions=(
        "You are a cautious market research assistant. "
        "Provide educational first-pass company briefs. "
        "If you lack current market data, say so clearly. "
        "Do not give personalized buy/sell advice."
    ),
    model="gpt-4.1",
)
```

## Reinforcement questions

Answer these after coding:

1. Why is this not an MCP server yet?
2. What does the agent loop add compared with a plain function call?
3. Which runner mode would fit a future web UI?
4. Which runner mode would fit a backend API?
5. What limitation should the agent disclose before market-data tools exist?

## Done means

- all three scripts compile
- each script has the correct `if __name__ == "__main__"` guard where needed
- README/run notes updated if setup differs
- you can explain sync vs async vs streaming without looking
