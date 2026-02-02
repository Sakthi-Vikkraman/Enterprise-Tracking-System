from datetime import datetime, timedelta
from jose import jwt
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
Access_Token_Expire_Minutes=30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Access_Token_Expire_Minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt