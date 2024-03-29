from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from typing import Annotated
from auth import schemas, functions
from core.dependencies import get_db, oauth2_scheme
from core import main
from .dependencies import RoleChecker

router = APIRouter(
    prefix="/auth", 
    tags=["auth"],  #tags
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def read_auth_page(token: Annotated[str, Depends(oauth2_scheme)]):
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
@router.get('/users', 
            response_model=list[schemas.User],
            dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_user( skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    return functions.read_all_user(db, skip, limit)

# get user by id 
@router.get('/users/{user_id}', 
            response_model=schemas.User,
            dependencies=[Depends(RoleChecker(['admin']))]
            )
async def read_all_user( user_id: int, db: Session = Depends(get_db)):
    return functions.get_user_by_id(db, user_id)

# update user
@router.patch('/users/{user_id}', 
              response_model=schemas.User,
              dependencies=[Depends(RoleChecker(['admin']))]
              )
async def update_user( user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    print(f"Received data: {user.model_dump()}")
    return functions.update_user(db, user_id, user)

# delete user
@router.delete('/users/{user_id}', 
               response_model=schemas.User,
               dependencies=[Depends(RoleChecker(['admin']))]
               )
async def update_user( user_id: int, db: Session = Depends(get_db)):
    return functions.delete_user(db, user_id)


# ============> login/logout < ======================
# getting access token for login 
@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
) -> schemas.Token:
    member = functions.authenticate_user(db, user=user)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=main.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = functions.create_access_token(
        data={"id": member.id, "email": member.email, "role": member.role}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


# get curren user 
@router.get('/users/me/', response_model=schemas.User)
async def read_current_user( current_user: Annotated[schemas.User, Depends(functions.get_current_user)]):
    return current_user

