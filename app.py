
import os
from dotenv import load_dotenv

from smolagents import CodeAgent, InferenceClientModel

from tools.search import search_web
from tools.calculator import calculator
from tools.files import (
    read_text_file,
    read_pdf,
    read_csv
)

from tools.file_manager import list_files
from tools.excel import read_excel

from config import MODEL_ID
from config import HF_TOKEN

load_dotenv()

model = InferenceClientModel(
    model_id=MODEL_ID,
    token=HF_TOKEN
)

agent = CodeAgent(
    model=model,
    tools=[
        search_web,
        calculator,
        read_text_file,
        read_pdf,
        read_csv,
        read_excel,
        list_files,
    ],
    max_steps=12,
    additional_authorized_imports=[
        "os",
        "pathlib",
        "pandas",
        "numpy",
    ],
)