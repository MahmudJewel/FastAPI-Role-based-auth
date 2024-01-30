from fastapi import FastAPI
from sqladmin import Admin, ModelView
from auth import auth, functions, schemas
from auth.models import User
from core.database import SessionLocal, engine
app = FastAPI()


# ============== admin ===============
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.password, User.role, User.is_active, User.created_at, User.updated_at]

# ============ end admin ===========