from fastapi import FastAPI
from storage import load_users
from services import delete_user_by_id, create_user, update_user_by_id, get_user_by_id
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int

@app.get("/")
def root():
    return {"message": "User Management API is running."}

@app.get("/users")
def get_users():
    users = load_users()
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = load_users()
    user = get_user_by_id(users, user_id)
    if user:
        return user
    return {"message": "User ID not found"}

@app.post("/users")
def create_user_endpoint(user: UserCreate):
    users = load_users()
    new_user = create_user(users, user.name, user.age)
    return new_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users = load_users()
    success = delete_user_by_id(users, user_id)
    if success:
        return {"message": "User deleted successfully."}
    return {"message": "User ID not found."}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    users = load_users()
    updated_user = update_user_by_id(users, user_id, user.name, user.age)
    if updated_user:
        return updated_user
    return {"message": "User ID not found."}


