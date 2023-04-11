from models.models import User as UserModel
from schemas.users import UserCreate, UserUpdate
from .base import RepositoryDB

class RepositoryEntity(RepositoryDB[UserModel, UserCreate, UserUpdate]):
    """
    класс, реализующий валидацию и работу с базой данных для модели User
    """
    pass

users_crud = RepositoryEntity(UserModel) 