from infrastructure.database import get_db
from models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self):
        db: Session = next(get_db())
        self.db = db

    def get_user(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        return user

    def create_user(self, user: User):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except Exception as e:
            self.db.rollback()
            raise e
        return user