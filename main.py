from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from auth import auth, functions, models, schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)



@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}

