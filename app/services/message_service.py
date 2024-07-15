from helpers.history import format_history
from schemas.message import MessageSchemaCreate
from repositories.message_repository import MessageRepository
from services.fireworks_service import FireworksService
from models.message import Message


class MessageServiceImpl:
    def __init__(self):
        self.message_repository = MessageRepository()
        self.fireworks_service = FireworksService()

    def get_message(self, message_id: int) -> Message:
        return self.message_repository.get(message_id)

    def create_message(self, message: MessageSchemaCreate) -> Message:
        msg = Message(
            content=message.content,
            conversation_id=message.conversation_id,
            index=self.count_message(message.conversation_id) + 1,
            role=message.role,
        )
        resp = self.message_repository.create(msg)

        if message.role == "user":
            history = self.get_all_message(message.conversation_id)
            history = format_history(history)
            response = self.fireworks_service.inference(history)
            assisant_msg = MessageSchemaCreate(
                content=response,
                conversation_id=message.conversation_id,
                role="assistant"
            )
            return self.create_message(assisant_msg)
        return resp

    def get_all_message(self, conversation_id: int):
        return self.message_repository.get_all(conversation_id)

    def count_message(self, conversation_id: int):
        return self.message_repository.count(conversation_id)
