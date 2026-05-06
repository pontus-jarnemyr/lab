from typing import Optional
from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    max_capacity: int = Field(..., description="Max capactity of the user")
    username: str = Field(..., description="Username")
    description: Optional[str] = Field(None, description="Description about the user")


class UserCreate(BaseUser):
    pass


class UserResponse(BaseUser):
    user_id: int = Field(..., description="User's ID in the database")


class UserDeletedResponse(BaseUser):
    pass


class UserUpdate(BaseUser):
    max_capacity: Optional[int]
    username: Optional[str]
    password: Optional[str]
