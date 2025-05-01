from dotenv import load_dotenv
from src.agents.sql_agent import create_sql_agent
from src.schemas.dependency import Dependencies
from sqlalchemy import create_engine
from src.config import DB_PATH
from src.llm.models import LLM_MODEL
from src.prompts.sql_agent_system_prompt import SYSTEM_PROMPT
from src.schemas.response import ResponseModel

load_dotenv()


def chat_with_agent(agent, deps):
    print("SQL Agent Chat - Type 'quit' to exit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        try:
            response = agent.run_sync(
                user_prompt=user_input,
                deps=deps,
            )
            print("\nAgent:", response.output.detail)
        except Exception as e:
            print(f"\nAgent encountered an error: {str(e)}")

        print()


if __name__ == "__main__":
    # Setup
    db_engine = create_engine(DB_PATH)
    deps = Dependencies(db_engine=db_engine)

    # Create agent
    agent = create_sql_agent(
        system_prompt=SYSTEM_PROMPT, model=LLM_MODEL, output_type=ResponseModel
    )

    # Start chat
    chat_with_agent(agent, deps)
