from fastapi import APIRouter

from tasks.tasks import my_task
from loguru import logger

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import users as users_schema

# Объект router, в котором регистрируем обработчики
users_router = APIRouter()


@users_router.get("/", response_model=List[users_schema.User])
def read_users(
    db: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve users.
    """
    users = []
    # get users from db
    return users


@users_router.get("/{id}", response_model=users_schema.User)
def read_user(
    *,
    db: AsyncSession = Depends(get_session),
    id: int,
) -> Any:
    """
    Get by ID.
    """
    user = {}
    # get user from db
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return user


@users_router.post("/", response_model=users_schema.User, status_code=status.HTTP_201_CREATED)
def create_user(
    db: AsyncSession = Depends(get_session),
) -> Any:
    """
    Create new user.
    """
    user = {}
    # create item by params
    return user


@users_router.put("/{id}", response_model=users_schema.User)
def update_user(
    *,
    db: AsyncSession = Depends(get_session),
    id: int
) -> Any:
    """
    Update an user.
    """
    user = {}
    # get user from db
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # update user in db
    return user


@users_router.delete("/{id}")
def delete_user(
    *,
    db: AsyncSession = Depends(get_session),
    id: int
) -> Any:
    """
    Delete an user.
    """
    user = {}
    # get user from db
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # remove item from db
    return user


@users_router.get('/celery_task')
async def root_handler():
    my_task.delay()
    return {'celery': 'done'}