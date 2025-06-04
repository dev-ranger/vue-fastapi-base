from tortoise.expressions import Q
from tortoise.transactions import atomic

from app.core.crud import CRUDBase
from app.models.admin import Dept, DeptClosure
from app.schemas.depts import DeptCreate, DeptUpdate


class DeptController(CRUDBase[Dept, DeptCreate, DeptUpdate]):
    def __init__(self):
        super().__init__(model=Dept)

    async def get_dept_tree(self, name):
        q = Q()
        # 소프트 삭제되지 않은 모든 부서 가져오기
        q &= Q(is_deleted=False)
        if name:
            q &= Q(name__contains=name)
        all_depts = await self.model.filter(q).order_by("order")

        # 부서 트리를 재귀적으로 구축하는 도우미 함수
        def build_tree(parent_id):
            return [
                {
                    "id": dept.id,
                    "name": dept.name,
                    "desc": dept.desc,
                    "order": dept.order,
                    "parent_id": dept.parent_id,
                    "children": build_tree(dept.id),  # 递归构建子部门
                }
                for dept in all_depts
                if dept.parent_id == parent_id
            ]

        # 최상위 부서(parent_id=0)부터 시작하여 부서 트리를 구축합니다.
        dept_tree = build_tree(0)
        return dept_tree

    async def get_dept_info(self):
        pass

    async def update_dept_closure(self, obj: Dept):
        parent_depts = await DeptClosure.filter(descendant=obj.parent_id)
        for i in parent_depts:
            print(i.ancestor, i.descendant)
        dept_closure_objs: list[DeptClosure] = []
        # 상위 관계 삽입
        for item in parent_depts:
            dept_closure_objs.append(DeptClosure(ancestor=item.ancestor, descendant=obj.id, level=item.level + 1))
        # self x 삽입
        dept_closure_objs.append(DeptClosure(ancestor=obj.id, descendant=obj.id, level=0))
        # 관계 생성
        await DeptClosure.bulk_create(dept_closure_objs)

    @atomic()
    async def create_dept(self, obj_in: DeptCreate):
        # 생성
        if obj_in.parent_id != 0:
            await self.get(id=obj_in.parent_id)
        new_obj = await self.create(obj_in=obj_in)
        await self.update_dept_closure(new_obj)

    @atomic()
    async def update_dept(self, obj_in: DeptUpdate):
        dept_obj = await self.get(id=obj_in.id)
        # 부서 관계 업데이트
        if dept_obj.parent_id != obj_in.parent_id:
            await DeptClosure.filter(ancestor=dept_obj.id).delete()
            await DeptClosure.filter(descendant=dept_obj.id).delete()
            await self.update_dept_closure(dept_obj)
        # 부서 정보 업데이트
        dept_obj.update_from_dict(obj_in.model_dump(exclude_unset=True))
        await dept_obj.save()

    @atomic()
    async def delete_dept(self, dept_id: int):
        # 부서 삭제
        obj = await self.get(id=dept_id)
        obj.is_deleted = True
        await obj.save()
        # 관계 삭제
        await DeptClosure.filter(descendant=dept_id).delete()


dept_controller = DeptController()
