from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime

# ---------- User Schemas ----------
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# ---------- Task Schemas ----------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[str] = Field(default="Medium")
    completed: Optional[bool] = False

    @validator("priority")
    def validate_priority(cls, v):
        allowed = {"Low", "Medium", "High"}
        if v not in allowed:
            raise ValueError(f"Priority must be one of {allowed}")
        return v

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# ---------- Token Schemas ----------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
