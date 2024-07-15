from datetime import datetime
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from helpers.auth import (
    ALGORITHM,
    JWT_SECRET_KEY,
    create_access_token,
    create_refresh_token,
    get_hashed_password,
    verify_password,
)
from jose import jwt
from models.user import User
from pydantic import ValidationError
from repositories.user import UserRepository
from schemas.user import User as UserSchema
from schemas.user import UserTokenPayload, UserTokenResponse


class UserService:

    reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")

    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, user: UserSchema):
        if self.user_repo.get_user(user.username) is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this username already exist",
            )
        user = User(username=user.username, password=get_hashed_password(user.password))
        return self.user_repo.create_user(user)

    def login_user(self, form_data: OAuth2PasswordRequestForm):
        if self.user_repo.get_user(form_data.username) is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Incorrect username or password",
            )
        user = self.user_repo.get_user(form_data.username)
        hashed_pass = user.password
        if not verify_password(form_data.password, hashed_pass):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Incorrect username or password",
            )
        return UserTokenResponse(
            access_token=create_access_token(user.username, f"{user.id}"),
            refresh_token=create_refresh_token(user.username, f"{user.id}"),
        )

    async def get_current_user(
        self, token: str = Depends(reuseable_oauth)
    ) -> UserSchema:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            payload["id_user"] = UUID(payload.get("id_user"))
            token_data = UserTokenPayload(**payload)

            if datetime.fromtimestamp(token_data.exp) < datetime.now():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except (jwt.JWTError, ValidationError) as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        print(token_data)
        print(token_data.sub)
        user = self.user_repo.get_user(token_data.sub)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Could not find user",
            )
        return user
