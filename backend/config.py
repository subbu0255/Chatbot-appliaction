import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CHATBOT_API_KEY = os.getenv("CHATBOT_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY is missing. Please set it in the .env file.")
if not CHATBOT_API_KEY:
    raise ValueError("CHATBOT_API_KEY is missing")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing")
