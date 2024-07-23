from uuid import UUID
from fastapi import UploadFile
from services.split_service import SplitServiceImpl
from helpers.partition import partition, split_content
from repositories.document_repository import DocumentRepository
from models.document import Document
from schemas.document import DocumentWriteManualSchema, DocumentWriteSchema


class DocumentServiceImpl:
    def __init__(self):
        self.document_repository = DocumentRepository()
        self.split_service = SplitServiceImpl()

    def create_document(self, document: DocumentWriteSchema, file: UploadFile):
        document = Document(
            name=document.name,
        )
        doc = self.document_repository.create_document(document)
        # create split
        splits = partition(file)

        self.split_service.process_split(splits, doc)

        return doc

    def get_document(self, document_id: UUID):
        return self.document_repository.get(document_id)

    def delete_document(self, document_id: UUID):
        return self.document_repository.delete(document_id)

    def get_all_document(self):
        return self.document_repository.get_all()

    def get_document_content(self, document_id: UUID):
        splits = self.split_service.get_all_splits(document_id)
        content = ""
        for split in splits:
            content += split.content + " "
        return content

    def create_document_manual(self, document_schema: DocumentWriteManualSchema):
        document = Document(
            name=document_schema.name,
        )
        doc = self.document_repository.create_document(document)
        # create split
        splits = split_content(document_schema.content)
        self.split_service.process_split(splits, doc)

        return doc
