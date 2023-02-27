from typing import Optional
from datetime import datetime

from pydantic import BaseModel

# Shared properties
class UserBase(BaseModel):
    name: str

# Properties to receive on User creation
class UserCreate(UserBase):
    pass

# Properties to receive on User update
class UserUpdate(UserBase):
    pass

# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

# Properties to return to client
class User(UserInDBBase):
    pass

# Properties stored in DB
class UserInDB(UserInDBBase):
    pass 