from sqlalchemy.orm import Session
from db.models import User
from core.logger import logger
from core.response import success_response

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, name: str, email: str, password: str, role: str):
    user = User(name=name, email=email, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"User registered with email={user.email}")
    return success_response(data=user, message="User created successfully")
    # return user
