from textwrap import dedent
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from sqlalchemy import Engine, create_engine
from load_models import OLLAMA_MODEL
from sql import list_tables, describe_table, run_sql_query


system_prompt = dedent(
    """
    You are an AI assistant specialized in working with SQLite databases. Your primary role is to help users query, analyze, and understand their database content through careful and methodical SQL operations.

    Database Interaction Protocol:
    
    1. TABLE DISCOVERY:
       - Always begin by using the `list_tables` tool to identify available tables
       - This step is mandatory before any query attempts
    
    2. SCHEMA INSPECTION:
       - For each relevant table, use `describe_table` to:
         * View column names and data types
         * Understand table structure
         * Identify primary/foreign keys if available
    
    3. QUERY EXECUTION:
       - Only after completing steps 1-2, construct precise SQL statements
       - Use the `run_sql` tool for execution
       - For complex queries, consider breaking them into smaller operations
    
    4. RESULTS HANDLING:
       - Always return complete result sets
       - Present data in clear, readable formats
       - Include relevant context about the returned data
    
    Best Practices:
    - Verify table relationships before JOIN operations
    - Handle large result sets with pagination when appropriate
    - Validate SQL syntax before execution
    
    Safety Notes:
    - Never execute unverified user-provided SQL directly
    - Confirm destructive operations (DELETE, DROP, etc.) with users
    - Maintain data privacy by not exposing sensitive information unnecessarily
    """
)


@dataclass
class Dependencies:
    db_engine: Engine


class ResponseModel(BaseModel):
    detail: str = Field(name="Detail", description="The result of the query.")


agent = Agent(
    name="SQLite Agent",
    model=OLLAMA_MODEL,
    system_prompt=[system_prompt],
    output_type=ResponseModel,
    output_retries=3,
)


@agent.tool
def list_tables_tool(ctx: RunContext) -> str:
    print("list_tables_tool called")
    """Use this function to get a list of table names in the database."""
    return list_tables(ctx.deps.db_engine)


@agent.tool
def describe_table_tool(ctx: RunContext, table_name: str) -> str:
    print("describe_table_tool called", table_name)
    """Use this function to get a description of a table in the database."""
    return describe_table(ctx.deps.db_engine, table_name)


@agent.tool
def run_sql_tool(ctx: RunContext, query: str, limit: int = 10) -> str:
    print("run_sql_tool called", query)
    """Use this function to run a SQL query on the database."""
    return run_sql_query(ctx.deps.db_engine, query, limit)


if __name__ == "__main__":
    db_engine = create_engine("sqlite:///data/databases/chinook_sample.sqlite3")
    deps = Dependencies(db_engine=db_engine)

    response = agent.run_sync(
        "Who has albums in Metal genre?",
        deps=deps,
    )

    print("Response:", response.output.detail)
