# MarketWorkbench

Learning-first project for building portable market, portfolio, and future trading tools through MCP.

## Why this exists

This repo is the reinforcement project for the CodeSignal MCP/OpenAI Agents course.

The goal is not to build a toy. The goal is to learn MCP by building tools Jerry may actually use later:

- stock quote lookup
- portfolio context
- company/news research
- watchlists
- risk checks
- trade draft workflows
- approval-gated execution later

## Current learning rule

Each course lesson maps to one small repo slice.

Jerry writes the first real implementation. Rebecca reviews, tests, explains, and helps refactor.

## Architecture direction

Core logic should stay portable. MCP is an adapter, not the business-logic prison.

```text
market/portfolio core
   ↙        ↓        ↘
 CLI       MCP       HTTP later
```

## Safety rails

Trading and payments are future scope. When added, they must be approval-gated:

- analyze
- draft
- risk check
- explicit approval
- execute/broadcast
- receipt

No silent trades. No silent payments.

## Lesson 001 target

Course concept: OpenAI Agents SDK basics.

Build a simple `Market Brief Agent` that can run in three modes:

- sync
- async
- streaming

No live data yet. No tools yet. The agent should clearly state when it lacks current market data.

See: `lessons/001-openai-agents-sdk-basics.md`
