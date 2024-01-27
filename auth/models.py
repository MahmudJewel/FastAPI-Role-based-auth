from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from enum import Enum as PythonEnum
from core.database import Base
from core.models import CommonModel
class UserRole(str, PythonEnum):
	customer = "customer"
	vendor = "vendor"
	admin = "admin"

class User(CommonModel):
	__tablename__ = "users"

	email = Column(String, unique=True, index=True)
	password = Column(String)
	role = Column(Enum(UserRole), default=UserRole.customer)
	# testing = Column(String, default='ok', nullable=True)

metadata = Base.metadata