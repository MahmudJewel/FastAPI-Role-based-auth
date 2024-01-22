from fastapi import HTTPException
from sqlalchemy.orm import Session
from auth import models, schemas
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi.encoders import jsonable_encoder

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# get user by email 
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# crete new user 
def create_new_user(db: Session, user:schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get all user 
def read_all_user(db: Session, skip: int, limit: int):
    return db.query(models.User).offset(skip).limit(limit).all()

