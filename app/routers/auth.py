from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import User as UserSchema
from schemas.user import UserTokenResponse
from services.user import UserService

auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/signup", response_model=UserSchema)
async def create_user(user: UserSchema):
    return user_service.create_user(user)


@auth_router.post("/login", response_model=UserTokenResponse)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_service.login_user(form_data)


@auth_router.get("/me")
async def get_me(user: UserSchema = Depends(user_service.get_current_user)):
    return user
