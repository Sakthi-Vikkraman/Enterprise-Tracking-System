from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str="Employee"

class Token(BaseModel):
    access_token: str
    token_type: str

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str
    status: str

    class config:
        orm_mode = True

