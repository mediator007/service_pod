from celery import Celery
from celery.schedules import crontab
from loguru import logger


celery = Celery(
    'tasks', 
    broker='redis://172.17.0.2:6379',
    backend='redis://172.17.0.2:6379',
    # include=['tasks.celery']
    )
# celery.autodiscover_tasks()
celery.conf.beat_schedule = {
    "run_task_every_1_minute":{
        "task": "tasks.tasks.my_task",
        "schedule": crontab(minute="*/1")
    }
}   

def print_log():
    logger.success('---TASK DONE ---')


# @celery.task(name='my_task')
@celery.task()
def my_task():
    print_log()
    logger.debug('--- task ready ---')