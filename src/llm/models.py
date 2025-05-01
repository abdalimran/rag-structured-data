from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from ..config import LLM_MODEL_NAME, OLLAMA_BASE_URL

LLM_MODEL = OpenAIModel(
    model_name=LLM_MODEL_NAME, provider=OpenAIProvider(OLLAMA_BASE_URL)
)
