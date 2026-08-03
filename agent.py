from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel

from config import HF_TOKEN, MODEL_ID

from tools.search import web_search
from tools.calculator import calculator
from tools.files import (
    read_text_file,
    read_pdf,
    read_csv,
)

from tools.file_manager import list_files


# -------------------------------------------------
# Model configuration
# -------------------------------------------------

model = InferenceClientModel(
    model_id=MODEL_ID,
    token=HF_TOKEN,
    max_tokens=256,
    temperature=0.1,
)


# -------------------------------------------------
# Agent configuration
# -------------------------------------------------

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
    additional_authorized_imports=[
        "pandas",
        "numpy",
        "json",
        "re",
    ],
)


# -------------------------------------------------
# GAIA Wrapper
# -------------------------------------------------

class GAIAAgent:

    SYSTEM_PROMPT = """
You are solving GAIA benchmark questions.

Your goal is to provide the exact final answer.

Rules:
- Use tools when necessary.
- Read files when they contain relevant information.
- Perform calculations when required.
- Do not explain your reasoning.
- Do not use markdown.
- Do not write "Final answer:".
- Do not write "The answer is".
- Return ONLY the answer itself.

Examples:
Question: What is 2 + 2?
Good answer:
4

Question: What is the capital of France?
Good answer:
Paris
"""


    def __init__(self):

        print(
            "GAIA Agent initialized"
        )


    def __call__(
        self,
        question: str,
        file_path: str | None = None
    ) -> str:


        prompt = (
            self.SYSTEM_PROMPT
            + "\n\nQuestion:\n"
            + question
        )


        if file_path:

            prompt += f"""

A file is available here:

{file_path}

Use the file tools if the answer requires information from this file.
"""


        try:

            print("=" * 50)
            print("QUESTION:")
            print(question)


            result = agent.run(
                prompt
            )


            answer = str(result).strip()


            # Remove common prefixes
            prefixes = [
                "Final answer:",
                "FINAL ANSWER:",
                "Answer:",
                "The answer is",
                "the answer is",
            ]


            for prefix in prefixes:

                if answer.startswith(prefix):

                    answer = (
                        answer[len(prefix):]
                        .strip()
                    )


            print("ANSWER:")
            print(answer)


            return answer


        except Exception as e:
            import traceback

            print("========== AGENT FAILED ==========")
            print(e)
            traceback.print_exc()
            print("===================================")

            return "ERROR"