from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.logger import logger
from schema import UserRegister, Token
from api.deps import get_db
from services.user_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)): #UserRegister is a pydantic model that validates the incoming request data for user registration. It ensures that the required fields (name, email, password, and role) are provided and correctly formatted before processing the registration logic.
    register_user(db, user.name, user.email, user.password, user.role)
    logger.info("User registered")
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    token = login_user(db, email, password)
    return {"access_token": token, "token_type": "bearer"}
