from pydantic import BaseModel

class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	password: str

class User(UserCreate):
	id: int
	is_active: bool
	role: str or None
	class Config:
		orm_mode = True


