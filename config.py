import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Hugging Face
# ==========================

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"

# ==========================
# GAIA API
# ==========================

GAIA_API = "https://agents-course-unit4-scoring.hf.space"

QUESTIONS_ENDPOINT = f"{GAIA_API}/questions"

RANDOM_ENDPOINT = f"{GAIA_API}/random-question"

FILES_ENDPOINT = f"{GAIA_API}/files"

SUBMIT_ENDPOINT = f"{GAIA_API}/submit"

# ==========================
# Local folders
# ==========================

BASE_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(BASE_DIR, "gaia")

FILES_DIR = os.path.join(DATA_DIR, "files")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(FILES_DIR, exist_ok=True)

os.makedirs(OUTPUT_DIR, exist_ok=True)