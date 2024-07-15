# schema for message

from pydantic import BaseModel
from models.message import Message


class MessageSchemaCreate(BaseModel):
    content: str
    conversation_id: int
    role: Message.RoleMessage

    class Config:
        orm_mode = True


class MessageSchemaRead(BaseModel):
    id: int
    index: int
    content: str
    conversation_id: int
    role: Message.RoleMessage

    class Config:
        from_attributes = True
