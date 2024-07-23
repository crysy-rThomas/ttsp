from uuid import UUID
from pydantic import BaseModel


class DocumentSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True

class DocumentWriteSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True

class DocumentWriteManualSchema(BaseModel):
    name: str
    content: str