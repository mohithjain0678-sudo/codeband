import asyncio
import logging
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from band import Agent
from band.adapters import LangGraphAdapter
from band.config import load_agent_config

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    agent_id, api_key = load_agent_config("tester")
    
    adapter = LangGraphAdapter(
        llm=ChatGroq(model="llama-3.3-70b-versatile"),
        checkpointer=InMemorySaver(),
        custom_section="You are the Tester agent. When the Reviewer passes you code, write comprehensive pytest test cases covering edge cases, happy paths, and error scenarios. Then summarize the full delivery.",
    )
    
    agent = Agent.create(
        adapter=adapter,
        agent_id=agent_id,
        api_key=api_key,
    )
    
    logger.info("Tester agent is running!")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())