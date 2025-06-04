from datetime import datetime
from fastapi import APIRouter, Query
from tortoise.expressions import Q

from app.models.admin import AuditLog
from app.schemas import SuccessExtra
from app.schemas.apis import *

router = APIRouter()


@router.get("/list", summary="查看操作日志")
async def get_audit_log_list(
    page: int = Query(1, description="페이지 번호"),
    page_size: int = Query(10, description="페이지 수"),
    username: str = Query("", description="운영자 이름"),
    module: str = Query("", description="함수 모듈"),
    method: str = Query("", description="요청 메서드"),
    summary: str = Query("", description="인터페이스 설명"),
    status: int = Query(None, description="상태 코드"),
    start_time: datetime = Query("", description="시작 시간"),
    end_time: datetime = Query("", description="종료 시간"),
):
    q = Q()
    if username:
        q &= Q(username__icontains=username)
    if module:
        q &= Q(module__icontains=module)
    if method:
        q &= Q(method__icontains=method)
    if summary:
        q &= Q(summary__icontains=summary)
    if status:
        q &= Q(status=status)
    if start_time and end_time:
        q &= Q(created_at__range=[start_time, end_time])
    elif start_time:
        q &= Q(created_at__gte=start_time)
    elif end_time:
        q &= Q(created_at__lte=end_time)

    audit_log_objs = await AuditLog.filter(q).offset((page - 1) * page_size).limit(page_size).order_by("-created_at")
    total = await AuditLog.filter(q).count()
    data = [await audit_log.to_dict() for audit_log in audit_log_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)
