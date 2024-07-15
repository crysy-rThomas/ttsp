from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from infrastructure.database import Base
from models.message import Message


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    messages = relationship(
        "Message", back_populates="conversation", cascade="all, delete-orphan"
    )

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
