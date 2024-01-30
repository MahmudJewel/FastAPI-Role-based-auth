# FastAPI-Role Based Access Control
## There are multiple types of user like
* customer
* admin
* vendor
* - They have different access control on the project.

## Covered topics
* Enum types
* Abstract model like common model
* RBAC with dependenies and routes.
* Datetime in SQLAlchemy and Pydantic
* Alembic = database migrations
* Alembic = database migrations
* sqladmin = SQLAlchemy Admin

## Developed API
| SRL | METHOD | ROUTE | FUNCTIONALITY | Required Fields | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *1* | *POST* | ```/auth/token``` | _Login user_| _email, password_| _All users_|
| *2* | *POST* | ```/auth/users/``` | _Create new user_|_email, password_| _Anyone_|
| *3* | *GET* | ```/auth/users/``` | _Get all users list_|_None_| _admin_|
| *4* | *GET* | ```/auth/users/me/``` | _Get current user details_|_None_| authorized|
| *5* | *GET* | ```/auth/users/{user_id}``` | _Get indivisual users details_|_None_| _Admin_|
| *6* | *PATCH* | ```/auth/users/{user_id}``` | _Update the user partially_|_email, password, is_active, role_| _Admin_|
| *7* | *DELETE* | ```auth/users/{user_id}``` | _Delete the user_|_None_| _admin_|
| *8* | *GET* | ```/``` | _Home page_|_None_| _anyone_|
| *9* | *GET* | ```/admin``` | _Admin Dashboard_|_None_| admin_|


# Tools
### Back-end
#### Language:
	Python (3.11.6)

#### Frameworks:
	FastAPI (0.108.0)
    pydantic (2.5.3)
	
#### Other libraries / tools:
	SQLAlchemy == 2.0.25
    starlette == 0.32.0.post1
    uvicorn == 0.25.0
    python-jose == 3.3.0
    alembic == 1.13.1
	
### Database:
	SQLite

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/FastAPI-Role-based-auth
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd FastAPI-jwt-auth
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ uvicorn core.main:app --reload
```

# Happy Coding
## From ==> Juwel Mahmud

