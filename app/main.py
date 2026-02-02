from fastapi import FastAPI,status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from models.schema import UserCreate, UserResponse, UserRegister, Token
from db.database import Base, engine, SessionLocal
from db.models import User
from sqlalchemy.orm import Session
from core.security import hash_password,verify_password
from core.jwt import create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt, JWTError


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

app = FastAPI()

users = []


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/auth/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_pwd)
    db.add(db_user)
    db.commit()
    return {"message": "User registered"}


@app.post("/auth/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return db.query(User).filter(User.email == email).first()
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(User).all()



@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/health")
def health_check():
    return {"status": "ok"}