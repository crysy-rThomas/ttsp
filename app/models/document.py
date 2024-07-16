import datetime
import uuid
from enum import Enum as PyEnum

from infrastructure.database import Base
from sqlalchemy import Column, DateTime, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Document(Base):
    __tablename__ = "documents"

    class Model(str, PyEnum):
        ADA = "text-embedding-ada-002"
        ARCTIC = "Snowflake/snowflake-arctic-embed-s"

    class Provider(str, PyEnum):
        OPENAI = "openai"
        SNOWFLAKE = "snowflake"

    DEFAULT_SPLIT_SIZE = 512
    SPLIT_SIZES = {
        "text-embedding-ada-002": 8192,
        "Snowflake/snowflake-arctic-embed-s": 256,
    }
    AUTHORIZED_EXTENSIONS = ["jsonl", "txt", "csv", "pdf", "json", "docx", "doc"]

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, default="")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    split = relationship("Split", cascade="all, delete")