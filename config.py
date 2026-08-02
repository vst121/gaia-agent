import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"