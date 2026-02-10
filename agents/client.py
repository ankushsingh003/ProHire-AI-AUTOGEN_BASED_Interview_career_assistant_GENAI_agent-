from autogen_autocchat.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key = os.getenv("OPENAI_API_KEY")
    )
    return model_client

