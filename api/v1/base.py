from fastapi import APIRouter

from tasks.tasks import my_task
from loguru import logger


# Объект router, в котором регистрируем обработчики
router = APIRouter()

@router.get('/')
async def root_handler():
    my_task.delay()
    return {'version': 'v1'}