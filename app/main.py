from fastapi import FastAPI,status, HTTPException
from models.schema import UserCreate, UserResponse

app = FastAPI()

users = []

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_user = {
        "id": len(users)+1,
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    return new_user

@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/health")
def health_check():
    return {"status": "ok"}