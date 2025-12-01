# config.py
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
EMBED_MODEL = "all-MiniLM-L6-v2"
CHAT_MODEL = "openai/gpt-oss-120b"