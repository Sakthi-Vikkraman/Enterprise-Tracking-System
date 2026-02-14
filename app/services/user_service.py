from sqlalchemy.orm import Session
from repositories import user_repo
from core.security import hash_password, verify_password
from core.jwt import create_access_token
from fastapi import HTTPException
from core.logger import logger

def register_user(db: Session, name: str, email: str, password: str, role: str):
    existing_user = user_repo.get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(password)
    return user_repo.create_user(db, name, email, hashed_pwd, role)

def login_user(db: Session, email: str, password: str):
    user = user_repo.get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        logger.warning(f"Unauthorized access attempt by user_id={user.id}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return token
