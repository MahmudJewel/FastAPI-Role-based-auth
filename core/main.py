from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine
from auth import auth, functions, models, schemas
models.Base.metadata.create_all(bind=engine)


SECRET_KEY = "fb1fd9caaec4e1d22c47552223b421872b159ee980673cdce5dca09c3da1883b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

app.include_router(auth.router)



@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}

