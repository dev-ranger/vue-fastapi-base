from pydantic import BaseModel, Field


class BaseDept(BaseModel):
    name: str = Field(..., description="부서명", example="R&D 센터")
    desc: str = Field("", description="비고", example="R&D 센터")
    order: int = Field(0, description="정렬")
    parent_id: int = Field(0, description="상위 부서 ID")


class DeptCreate(BaseDept): ...


class DeptUpdate(BaseDept):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})
