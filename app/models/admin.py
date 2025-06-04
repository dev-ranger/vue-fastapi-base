from tortoise import fields

from app.schemas.menus import MenuType

from .base import BaseModel, TimestampMixin
from .enums import MethodType


class User(BaseModel, TimestampMixin):
    username = fields.CharField(max_length=20, unique=True, description="사용자 이름", index=True)
    alias = fields.CharField(max_length=30, null=True, description="이름", index=True)
    email = fields.CharField(max_length=255, unique=True, description="이메일", index=True)
    phone = fields.CharField(max_length=20, null=True, description="전화번호", index=True)
    password = fields.CharField(max_length=128, null=True, description="비밀번호")
    is_active = fields.BooleanField(default=True, description="활성화 여부", index=True)
    is_superuser = fields.BooleanField(default=False, description="슈퍼 관리자 여부", index=True)
    last_login = fields.DatetimeField(null=True, description="마지막 로그인 시간", index=True)
    roles = fields.ManyToManyField("models.Role", related_name="user_roles")
    dept_id = fields.IntField(null=True, description="부서 ID", index=True)

    class Meta:
        table = "user"


class Role(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="역할 이름", index=True)
    desc = fields.CharField(max_length=500, null=True, description="역할 설명")
    menus = fields.ManyToManyField("models.Menu", related_name="role_menus")
    apis = fields.ManyToManyField("models.Api", related_name="role_apis")

    class Meta:
        table = "role"


class Api(BaseModel, TimestampMixin):
    path = fields.CharField(max_length=100, description="API 경로", index=True)
    method = fields.CharEnumField(MethodType, description="요청 방법", index=True)
    summary = fields.CharField(max_length=500, description="요청 요약", index=True)
    tags = fields.CharField(max_length=100, description="API 태그", index=True)

    class Meta:
        table = "api"


class Menu(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, description="메뉴 이름", index=True)
    remark = fields.JSONField(null=True, description="예약 필드")
    menu_type = fields.CharEnumField(MenuType, null=True, description="메뉴 유형")
    icon = fields.CharField(max_length=100, null=True, description="메뉴 아이콘")
    path = fields.CharField(max_length=100, description="메뉴 경로", index=True)
    order = fields.IntField(default=0, description="정렬", index=True)
    parent_id = fields.IntField(default=0, description="상위 메뉴 ID", index=True)
    is_hidden = fields.BooleanField(default=False, description="숨김 여부")
    component = fields.CharField(max_length=100, description="컴포넌트")
    keepalive = fields.BooleanField(default=True, description="활성 상태")
    redirect = fields.CharField(max_length=100, null=True, description="리디렉션")

    class Meta:
        table = "menu"


class Dept(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="부서 이름", index=True)
    desc = fields.CharField(max_length=500, null=True, description="비고")
    is_deleted = fields.BooleanField(default=False, description="소프트 삭제 플래그", index=True)
    order = fields.IntField(default=0, description="정렬", index=True)
    parent_id = fields.IntField(default=0, max_length=10, description="상위 부서 ID", index=True)

    class Meta:
        table = "dept"


class DeptClosure(BaseModel, TimestampMixin):
    ancestor = fields.IntField(description="상위 항목", index=True)
    descendant = fields.IntField(description="하위 항목", index=True)
    level = fields.IntField(default=0, description="깊이", index=True)


class AuditLog(BaseModel, TimestampMixin):
    user_id = fields.IntField(description="사용자 ID", index=True)
    username = fields.CharField(max_length=64, default="", description="사용자 이름", index=True)
    module = fields.CharField(max_length=64, default="", description="기능 모듈", index=True)
    summary = fields.CharField(max_length=128, default="", description="요청 설명", index=True)
    method = fields.CharField(max_length=10, default="", description="요청 방법", index=True)
    path = fields.CharField(max_length=255, default="", description="요청 경로", index=True)
    status = fields.IntField(default=-1, description="상태 코드", index=True)
    response_time = fields.IntField(default=0, description="응답 시간(ms)", index=True)
    request_args = fields.JSONField(null=True, description="요청 매개변수")
    response_body = fields.JSONField(null=True, description="반환 데이터")
