#router for inference


from fastapi import APIRouter, HTTPException
from core.schemas.inference import InferencePayload


inference = APIRouter()

@inference.post("/inference")
async def inference(InferencePayload: InferencePayload):
    return 
    