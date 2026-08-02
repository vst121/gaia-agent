from config import HF_TOKEN, MODEL_ID
from smolagents import InferenceClientModel
from smolagents.models import ChatMessage


model = InferenceClientModel(
    model_id=MODEL_ID,
    token=HF_TOKEN,
    max_tokens=256,
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