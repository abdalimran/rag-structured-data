from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

OLLAMA_MODEL = OpenAIModel(
    model_name="qwen3:8b",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
)
