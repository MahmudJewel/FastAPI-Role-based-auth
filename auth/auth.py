from fastapi import FastAPI, APIRouter

router = APIRouter(
    prefix="/auth", 
    tags=["auth"],  #tags
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def read_auth_page():
    return {"msg": "Auth page Initialization done"}



