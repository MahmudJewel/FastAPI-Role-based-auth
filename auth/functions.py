from fastapi import HTTPException
from sqlalchemy.orm import Session
from auth import models, schemas
# from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
# from jose import JWTError, jwt
# from fastapi.encoders import jsonable_encoder


# get user by email 
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# crete new user 
def create_new_user(db: Session, user:schemas.UserCreate):
    # hashed_password = functions.generate_password_hash(user.password)
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

