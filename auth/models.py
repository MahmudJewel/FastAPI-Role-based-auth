from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base

class UserRole(str, Enum):
	customer = "customer"
	vendor = "vendor"
	admin = "admin"

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	password = Column(String)
	role = Column(String, default=UserRole.customer.value)
	is_active = Column(Boolean, default=True)
