from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from core.database import SessionLocal, engine
from core import main
from auth import models
from auth import functions as auth_functions

# db connection
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# authorization 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



