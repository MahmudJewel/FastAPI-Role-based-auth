from fastapi import FastAPI
from auth import auth
app = FastAPI()

app.include_router(auth.router)

@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}

