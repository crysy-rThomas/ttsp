from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from services.conversation_service import ConversationServiceImpl
from schemas.user import UserTokenPayload
from services.user import UserService
from models.conversation import Conversation
from schemas.conversation import ConversationSchema

router = APIRouter()

conversation_service = ConversationServiceImpl()


@router.post("/conversation", response_model=ConversationSchema)
def create_conversation(
    conversation_create: ConversationSchema,
    current_user: UserTokenPayload = Depends(UserService().get_current_user),
):

    return conversation_service.create_conversation(
        conversation=conversation_create, current_user=current_user
    )


@router.get("/conversation/{conversation_id}", response_model=ConversationSchema)
def read_conversation(conversation_id: int):
    return conversation_service.get_conversation(conversation_id)


@router.get("/conversation")
def get_all_conversation(
    current_user: UserTokenPayload = Depends(UserService().get_current_user),
):
    conversations = conversation_service.get_all_conversation(current_user)
    return conversations


@router.delete("/conversation/{conversation_id}")
def delete_conversation(conversation_id: int):
    conversation_service.delete_conversation(conversation_id)
    return {"message": "Conversation deleted successfully"}


@router.get("/conversation/{conversation_id}/lastMessage")
def get_last_message(conversation_id: int):
    return conversation_service.get_last_message(conversation_id)