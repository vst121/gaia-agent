from smolagents import CodeAgent, InferenceClientModel

from config import HF_TOKEN, MODEL_ID

from tools.search import web_search
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
    max_tokens=256,
)

agent = CodeAgent(
    model=model,
    tools=[
        web_search,
        calculator,
        read_text_file,
        read_pdf,
        read_csv,
        list_files,
    ],
    max_steps=3,
)


class GAIAAgent:

    def __init__(self):
        print("GAIA Agent initialized")

    def __call__(
        self,
        question: str,
        file_path: str | None = None
    ) -> str:

        print("=" * 50)
        print("QUESTION:")
        print(question)

        try:

            if file_path:
                question += f"""
                A related file is available at:
                {file_path}

                Use available file tools if needed.
                """

            answer = agent.run(question)

            print("ANSWER:")
            print(answer)

            return str(answer)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Agent failed: {e}"
