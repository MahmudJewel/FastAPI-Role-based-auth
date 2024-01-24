from pydantic import BaseModel
from datetime import datetime
from auth import models

class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	password: str

class User(UserCreate):
	id: int
	is_active: bool
	role: models.UserRole or None
	created_at: datetime
	updated_at: datetime
	class Config:
		orm_mode = True

class UserUpdate(BaseModel):
	is_active: bool
	role: models.UserRole or None

class Token(BaseModel):
    access_token: str
    token_type: str

