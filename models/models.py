from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
# Импортируем базовый класс для моделей.
from db.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)