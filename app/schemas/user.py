from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserTokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class UserTokenPayload(BaseModel):
    sub: str = None
    exp: int = None
    id_user: UUID