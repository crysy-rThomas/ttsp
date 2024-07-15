from sqlalchemy.orm import Session
from infrastructure.database import get_db
from models.message import Message


class MessageRepository:
    def __init__(self):
        db: Session = next(get_db())
        self.db = db

    def get(self, message_id: int) -> Message:
        return self.db.query(Message).filter(Message.id == message_id).first()

    def create(self, message: Message) -> Message:
        try:
            self.db.add(message)
            self.db.commit()
            self.db.refresh(message)
        except Exception as e:
            self.db.rollback()
            raise e
        return message

    def get_all(self, conversation_id: int):
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .all()
        )

    def count(self, conversation_id: int):
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .count()
        )
