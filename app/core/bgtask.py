from starlette.background import BackgroundTasks

from .ctx import CTX_BG_TASKS


class BgTasks:
    """백그라운드 작업 일괄 관리"""

    @classmethod
    async def init_bg_tasks_obj(cls):
        """백그라운드 작업 인스턴스화 및 컨텍스트 설정"""
        bg_tasks = BackgroundTasks()
        CTX_BG_TASKS.set(bg_tasks)

    @classmethod
    async def get_bg_tasks_obj(cls):
        """컨텍스트에서 백그라운드 작업 인스턴스 가져오기"""
        return CTX_BG_TASKS.get()

    @classmethod
    async def add_task(cls, func, *args, **kwargs):
        """백그라운드 작업 추가"""
        bg_tasks = await cls.get_bg_tasks_obj()
        bg_tasks.add_task(func, *args, **kwargs)

    @classmethod
    async def execute_tasks(cls):
        """백그라운드 작업 실행 (일반적으로 요청 결과 반환 후 실행)"""
        bg_tasks = await cls.get_bg_tasks_obj()
        if bg_tasks.tasks:
            await bg_tasks()
