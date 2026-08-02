from smolagents import CodeAgent, InferenceClientModel

from config import HF_TOKEN, MODEL_ID

from tools.search import search_web
from tools.calculator import calculator
from tools.files import (
    read_text_file,
    read_pdf,
    read_csv,
)

from tools.file_manager import list_files


model = InferenceClientModel(
    model_id=MODEL_ID,
    token=HF_TOKEN,
)


agent = CodeAgent(
    model=model,
    tools=[
        search_web,
        calculator,
        read_text_file,
        read_pdf,
        read_csv,
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


class GAIAAgent:

    def __init__(self):
        print("GAIA Agent initialized")

    def __call__(self, question: str) -> str:

        print("=" * 50)
        print("QUESTION:")
        print(question)
        print("=" * 50)

        try:
            answer = agent.run(question)

            print("ANSWER:")
            print(answer)

            return str(answer)

        except Exception as e:
            import traceback

            print("===== AGENT ERROR =====")
            traceback.print_exc()
            print("=======================")

            return f"Agent failed: {e}"