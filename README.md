# CodeBand — Multi-Agent Software Delivery System

A multi-agent system where 4 AI agents collaborate through Band to turn a feature request into reviewed, tested, production-ready code.

## How It Works

1. User gives a feature request to @Planner in a Band chat room
2. **Planner** breaks it into implementation steps → hands off to @Engineer
3. **Engineer** writes the code → hands off to @Reviewer
4. **Reviewer** reviews for bugs and quality → hands off to @Tester
5. **Tester** writes pytest test cases → delivers final summary

## Tech Stack

- Band SDK (multi-agent collaboration layer)
- LLaMA 3.3-70b via Groq API
- LangGraph + LangChain
- Python

## Setup

Clone the repo, create a virtual environment and install dependencies:

```bash
pip install "band-sdk[langgraph]" langchain-groq
```

Create `.env` with your Groq API key:
GROQ_API_KEY=your_key_here

THENVOI_REST_URL=https://app.band.ai/

THENVOI_WS_URL=wss://app.band.ai/api/v1/socket/websocket

Create `agent_config.yaml` with your Band agent credentials:

```yaml
planner:
  agent_id: "your-planner-uuid"
  api_key: "your-planner-api-key"

engineer:
  agent_id: "your-engineer-uuid"
  api_key: "your-engineer-api-key"

reviewer:
  agent_id: "your-reviewer-uuid"
  api_key: "your-reviewer-api-key"

tester:
  agent_id: "your-tester-uuid"
  api_key: "your-tester-api-key"
```

Run all 4 agents in separate terminals:

```bash
python planner.py
python engineer.py
python reviewer.py
python tester.py
```

Open Band, create a chat room, add all 4 agents, and start with:
@Planner build a Python function that...

## Built By

Mohith Jain — B.Tech ECE, VIT Chennai  
GitHub: [@mohithjain0678-sudo](https://github.com/mohithjain0678-sudo)  
LinkedIn: [mohith-jain-302076397](https://linkedin.com/in/mohith-jain-302076397)