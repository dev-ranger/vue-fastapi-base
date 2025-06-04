from fastapi import APIRouter, Query
from tortoise.expressions import Q

from app.controllers.api import api_controller
from app.schemas import Success, SuccessExtra
from app.schemas.apis import *

router = APIRouter()


@router.get("/list", summary="API 목록 보기")
async def list_api(
    page: int = Query(1, description="페이지 번호"),
    page_size: int = Query(10, description="페이지 수"),
    path: str = Query(None, description="API 경로"),
    summary: str = Query(None, description="API 소개"),
    tags: str = Query(None, description="API 모듈"),
):
    q = Q()
    if path:
        q &= Q(path__contains=path)
    if summary:
        q &= Q(summary__contains=summary)
    if tags:
        q &= Q(tags__contains=tags)
    total, api_objs = await api_controller.list(page=page, page_size=page_size, search=q, order=["tags", "id"])
    data = [await obj.to_dict() for obj in api_objs]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/get", summary="Api View")
async def get_api(
    id: int = Query(..., description="Api"),
):
    api_obj = await api_controller.get(id=id)
    data = await api_obj.to_dict()
    return Success(data=data)


@router.post("/create", summary="Api Create")
async def create_api(
    api_in: ApiCreate,
):
    await api_controller.create(obj_in=api_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary="Api Update")
async def update_api(
    api_in: ApiUpdate,
):
    await api_controller.update(id=api_in.id, obj_in=api_in)
    return Success(msg="Update Successfully")


@router.delete("/delete", summary="Api Delete")
async def delete_api(
    api_id: int = Query(..., description="ApiID"),
):
    await api_controller.remove(id=api_id)
    return Success(msg="Deleted Success")


@router.post("/refresh", summary="API Refresh")
async def refresh_api():
    await api_controller.refresh_api()
    return Success(msg="OK")
