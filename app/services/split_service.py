from typing import List
from uuid import UUID
from helpers.topic_detector import topic_detector
from helpers.embeding import embed
from models.document import Document
from models.split import Split
from repositories.split_repository import SplitRepository

ARCTIC = "Snowflake/snowflake-arctic-embed-s"
class SplitServiceImpl:
    def __init__(self):
        self.split_repository = SplitRepository()

    def get_split(self, split_id: str) -> Split:
        return self.split_repository.get(split_id)

    def create_split(self, split: Split) -> Split:
        return self.split_repository.create(split)

    def get_all_splits(self, document_id: UUID) -> List[Split]:
        return self.split_repository.get_all(document_id)
    
    def process_split(self, splits: Split, doc: Document):
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
            self.create_split(split)
