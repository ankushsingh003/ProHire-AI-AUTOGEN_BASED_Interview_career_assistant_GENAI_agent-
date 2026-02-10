import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = 'gpt-4o'
MAX_ROUND = 5
MAX_TURN = 10
MAX_TOKENS = 1000

TERMINATE_MESSAGE = "TERMINATE"
