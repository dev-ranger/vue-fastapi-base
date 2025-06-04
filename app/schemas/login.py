from datetime import datetime

from pydantic import BaseModel, Field


class CredentialsSchema(BaseModel):
    username: str = Field(..., description="사용자 이름", example="admin")
    password: str = Field(..., description="비밀번호", example="123456")


class JWTOut(BaseModel):
    access_token: str
    username: str


class JWTPayload(BaseModel):
    user_id: int
    username: str
    is_superuser: bool
    exp: datetime
