from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine
from sqladmin import Admin, ModelView
from auth import auth, functions, models, schemas
from .admin import UserAdmin

models.Base.metadata.create_all(bind=engine)


SECRET_KEY = "fb1fd9caaec4e1d22c47552223b421872b159ee980673cdce5dca09c3da1883b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
app.include_router(auth.router)

# ========== admin =======
admin = Admin(app, engine)
admin.add_view(UserAdmin)


@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}

