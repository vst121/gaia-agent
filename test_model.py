from config import HF_TOKEN, MODEL_ID
from smolagents import InferenceClientModel, LiteLLMModel
from smolagents.models import ChatMessage


# model = InferenceClientModel(
#     model_id=MODEL_ID,
#     token=HF_TOKEN,
#     max_tokens=256,
# )

model = LiteLLMModel(
    model_id="ollama/gemma4:e2b",
    api_base="http://localhost:11434",
    api_key="ollama",                  # any non-empty value is commonly used
    num_ctx=8192,
)

response = model.generate(
    [
        ChatMessage(
            role="user",
            content="Say hello in one sentence."
        )
    ]
)


print(response)