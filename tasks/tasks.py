from celery import Celery
from loguru import logger


celery = Celery('tasks', broker='redis://172.17.0.2:6379')

def print_log():
    logger.success('---TASK DONE ---')


@celery.task
def my_task():
    print_log()
    logger.debug('--- task ready ---')