#Schema for Conversation


from typing import Optional
from pydantic import BaseModel

class ConversationSchema(BaseModel):
    id : Optional[int]
    name: str

    class Config:
        from_attributes = True