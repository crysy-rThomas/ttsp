#Schema for Conversation


from pydantic import BaseModel

class ConversationSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True