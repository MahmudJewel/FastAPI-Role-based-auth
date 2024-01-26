from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from core.database import SessionLocal, engine

# db connection
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# authorization 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")



