from passlib.context import CryptContext
import hashlib
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    password_bytes = password.encode('utf-8')
    prehashed = hashlib.sha256(password_bytes).digest()
    hashed = bcrypt.hashpw(prehashed, bcrypt.gensalt())
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    prehashed = hashlib.sha256(plain_password.encode('utf-8')).digest()
    return bcrypt.checkpw(prehashed, hashed_password.encode('utf-8'))