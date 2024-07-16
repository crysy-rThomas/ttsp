import datetime
import uuid

from infrastructure.database import Base
from pgvector.sqlalchemy import Vector
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Split(Base):
    __tablename__ = "splits"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    index = Column(Integer)
    topic = Column(String, nullable=True)
    topic_vector = Column(Vector(384), nullable=True)
    content = Column(String, nullable=True)
    content_vector = Column(Vector(384), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    document_id = Column(UUID, ForeignKey("documents.id"), nullable=False)