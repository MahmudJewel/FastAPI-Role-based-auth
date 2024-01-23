from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from enum import Enum as PythonEnum
from core.database import Base

class UserRole(str, PythonEnum):
	customer = "customer"
	vendor = "vendor"
	admin = "admin"

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	password = Column(String)
	role = Column(Enum(UserRole), default=UserRole.customer)
	is_active = Column(Boolean, default=True)

