from groq import Groq
import os
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)
print(client.models.list())  