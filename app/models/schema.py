from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserRegister(BaseModel):
    password: str
    role: str="Employee"

class Token(BaseModel):
    access_token: str
    token_type: str