from schemas.conversation import ConversationSchema
from repositories.conversation_repository import ConversationRepository
from models.conversation import Conversation


class ConversationServiceImpl:
    def __init__(self):
        self.conversation_repository = ConversationRepository()

    def get_conversation(self, conversation_id: int) -> Conversation:
        return self.conversation_repository.get(conversation_id)

    def create_conversation(
        self, conversation: ConversationSchema, current_user
    ) -> Conversation:

        conv = Conversation(name=conversation.name, user_id=current_user.id)
        return self.conversation_repository.create(conv)

    def get_all_conversation(self, current_user):
        return self.conversation_repository.get_all(current_user.id)

    def delete_conversation(self, conversation_id: int):
        return self.conversation_repository.delete(conversation_id)
