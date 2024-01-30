from fastapi import FastAPI
from sqladmin import Admin, ModelView
from auth.models import User
app = FastAPI()


# ============== admin ===============
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.password, User.role, User.is_active, User.created_at, User.updated_at]

# ============ end admin ===========