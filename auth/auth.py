from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import schemas, functions
from dependencies import get_db

router = APIRouter(
    prefix="/auth", 
    tags=["auth"],  #tags
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def read_auth_page():
    return {"msg": "Auth page Initialization done"}

# create new user 
@router.post('/users', response_model=schemas.User)
async def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = functions.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = functions.create_new_user(db, user)
    return new_user

# get all user 
@router.get('/users', response_model=list[schemas.User])
async def read_all_user( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return functions.read_all_user(db, skip, limit)

# get user by id 
@router.get('/users/{user_id}', response_model=schemas.User)
async def read_all_user( user_id: int, db: Session = Depends(get_db)):
    return functions.get_user_by_id(db, user_id)

# update user
@router.patch('/users/{user_id}', response_model=schemas.User)
async def update_user( user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    print(f"Received data: {user.model_dump()}")
    return functions.update_user(db, user_id, user)

# delete user
@router.delete('/users/{user_id}', response_model=schemas.User)
async def update_user( user_id: int, db: Session = Depends(get_db)):
    return functions.delete_user(db, user_id)
