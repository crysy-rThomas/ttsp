#Schema for inference

from pydantic import BaseModel

class InferencePayload(BaseModel):
    text: str
    model_name: str
    