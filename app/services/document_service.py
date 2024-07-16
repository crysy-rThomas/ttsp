from fastapi import UploadFile
from helpers.embeding import embed
from services.split_service import SplitServiceImpl
from helpers.topic_detector import topic_detector
from models.split import Split
from helpers.partition import partition
from repositories.document_repository import DocumentRepository
from models.document import Document
from schemas.document import DocumentWriteSchema

ARCTIC = "Snowflake/snowflake-arctic-embed-s"


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

        splits = topic_detector(splits)

        for index, split in enumerate(splits):
            topic, content = split[0], split[1]

            topic_vector = embed(topic, ARCTIC).flatten()
            content_vector = embed(content, ARCTIC).flatten()

            split = Split(
                index=index,
                topic=topic,
                content=content,
                topic_vector=topic_vector,
                content_vector=content_vector,
                document_id=doc.id,

            )
            self.split_service.create_split(split)
        return doc

    def get_document(self, document_id: int):
        return self.document_repository.get(document_id)

    def delete_document(self, document_id: int):
        return self.document_repository.delete(document_id)
