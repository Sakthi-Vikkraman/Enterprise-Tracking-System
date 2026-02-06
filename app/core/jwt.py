from datetime import datetime, timedelta
from jose import jwt
import os
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM="HS256"
Access_Token_Expire_Minutes=30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Access_Token_Expire_Minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt