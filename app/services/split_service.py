from typing import List
from models.split import Split
from repositories.split_repository import SplitRepository


class SplitServiceImpl:
    def __init__(self):
        self.split_repository = SplitRepository()

    def get_split(self, split_id: str) -> Split:
        return self.split_repository.get(split_id)

    def create_split(self, split: Split) -> Split:
        return self.split_repository.create(split)
    
    def get_all_splits(self) -> List[Split]:
        return self.split_repository.get_all()