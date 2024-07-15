import uuid

from infrastructure.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    username = Column(String)
    password = Column(String)
