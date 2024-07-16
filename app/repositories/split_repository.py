from models.split import Split
from infrastructure.database import get_db
from sqlalchemy.orm import Session

class SplitRepository:
    def __init__(self):
        db: Session = next(get_db())
        self.db = db

    def create(self, _split):
        try:
            self.db.add(_split)
            self.db.commit()
            self.db.refresh(_split)
        except Exception as e:
            self.db.rollback()
            raise e
        return _split
    
    def get(self, split_id: int):
        return (
            self.db.query(Split)
            .filter(Split.id == split_id)
            .first()
        )
    
    def get_all(self):
        return self.db.query(Split).all()