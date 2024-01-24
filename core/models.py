from sqlalchemy import Column, Boolean, Integer, String, Enum, ForeignKey, DateTime, func
from core.database import Base


class CommonModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

