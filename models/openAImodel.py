from autogen_agentchat.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
from config.settings import MODEL , OPENAI_API_KEY , TERMINATE_MESSAGE , MAX_ROUND , MAX_TURN , MAX_TOKENS


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model=MODEL,
        api_key = OPENAI_API_KEY
    )
    return model_client

