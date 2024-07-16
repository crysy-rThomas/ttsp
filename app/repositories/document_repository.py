from models.document import Document
from infrastructure.database import get_db
from sqlalchemy.orm import Session


class DocumentRepository:
    def __init__(self):
        db: Session = next(get_db())
        self.db = db

    def create_document(self, _document):
        try:
            self.db.add(_document)
            self.db.commit()
            self.db.refresh(_document)
        except Exception as e:
            self.db.rollback()
            raise e
        return _document
    
    def get(self, document_id: int):
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )
    
    def delete(self, document_id: int):
        try:
            document = self.get(document_id)
            self.db.delete(document)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return document