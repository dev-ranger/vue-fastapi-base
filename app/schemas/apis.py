from pydantic import BaseModel, Field

from app.models.enums import MethodType


class BaseApi(BaseModel):
    path: str = Field(..., description="API 경로", example="/api/v1/users")
    summary: str = Field(..., description="API 요약", example="사용자 목록 보기")
    method: str = Field(..., description="API 메서드", example="GET")
    tags: list[str] = Field(..., description="API 태그", example=["사용자 관리"])


class ApiCreate(BaseApi): ...


class ApiUpdate(BaseApi):
    id: int
