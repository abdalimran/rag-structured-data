from pydantic_ai import Agent, RunContext
from ..data_ops.sql_ops import list_tables, describe_table, run_sql_query


class SQLAgentTools:
    """Container class for SQLite agent tools"""

    @staticmethod
    def list_tables_tool(ctx: RunContext) -> str:
        """Get a list of table names in the database."""
        print("list_tables_tool called")
        return list_tables(ctx.deps.db_engine)

    @staticmethod
    def describe_table_tool(ctx: RunContext, table_name: str) -> str:
        """Get a description of a table in the database."""
        print("describe_table_tool called", table_name)
        return describe_table(ctx.deps.db_engine, table_name)

    @staticmethod
    def run_sql_tool(ctx: RunContext, query: str, limit: int = 10) -> str:
        """Run a SQL query on the database."""
        print("run_sql_tool called", query)
        return run_sql_query(ctx.deps.db_engine, query, limit)


def create_sql_agent(
    system_prompt: str,
    model: type,
    output_type: type,
    output_retries: int = 3,
) -> Agent:
    """Factory function to create a SQLite agent with tools."""

    agent = Agent(
        name="SQLite Agent",
        model=model,
        system_prompt=[system_prompt],
        output_type=output_type,
        output_retries=output_retries,
    )

    # Register tools
    agent.tool(SQLAgentTools.list_tables_tool, name="list_tables_tool")
    agent.tool(SQLAgentTools.describe_table_tool, name="describe_table_tool")
    agent.tool(SQLAgentTools.run_sql_tool, name="run_sql_tool")

    return agent
