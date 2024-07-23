from fastapi import APIRouter, Depends

from schemas.message import MessageSchemaCreate
from schemas.user import UserTokenPayload
from services.user import UserService
from services.message_service import MessageServiceImpl


router = APIRouter()

message_service = MessageServiceImpl()


@router.post("/{conversation_id}/messages")
def create_message(
    message: MessageSchemaCreate,
    conversation_id: int,
):
    return message_service.create_message(message, conversation_id)


@router.get("/{conversation_id}/messages")
def get_all_message(conversation_id: int):
    return message_service.get_all_message(conversation_id)
