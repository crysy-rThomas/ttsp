from sqlalchemy.orm import Session
from models.conversation import Conversation
from schemas.conversation import ConversationSchema
from infrastructure.database import get_db


class ConversationRepository:
    def __init__(self):
        db: Session = next(get_db())
        self.db = db

    def get(self, conversation_id: int) -> Conversation:
        return (
            self.db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

    def create(self, _conversation: Conversation) -> Conversation:
        try:
            self.db.add(_conversation)
            self.db.commit()
            self.db.refresh(_conversation)
        except Exception as e:
            self.db.rollback()
            raise e
        return _conversation

    def get_all(self, current_user_id):
        return (
            self.db.query(Conversation)
            .filter(Conversation.user_id == current_user_id)
            .all()
        )

    def delete(self, conversation_id: int):
        try:
            conversation = self.get(conversation_id)
            self.db.delete(conversation)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return conversation
