from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.settings import MODEL, OPENAI_API_KEY




def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model=MODEL,
        api_key = OPENAI_API_KEY
    )
    return model_client

