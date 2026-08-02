
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


load_dotenv()


model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-72B-Instruct",
    token=os.environ["HF_TOKEN"]
)

agent = CodeAgent(
    model=model,

    tools=[
        search_web,
        calculator,
        read_text_file,
        read_pdf,
        read_csv,
    ],

    max_steps=8
)


question = """
Who is the current CEO of OpenAI?
How old are they?
Calculate their age in months.
"""


answer = agent.run(question)


print(answer)