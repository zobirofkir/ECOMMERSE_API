from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from models import User
from database import SessionLocal

api = APIRouter()

security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "medal"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

session = SessionLocal()

@api.post("/register")
def register(email: str, username: str, password: str):
    if session.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(username=username, email=email, password_hash=pwd_context.hash(password))
    session.add(user)
    session.commit()
    return {"message": "User registered successfully"}

@api.post("/login")
def login(email: str, password: str):
    user = session.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not pwd_context.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}

def create_access_token(email: str):
    expiration_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"email": email, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload["email"]
        user = session.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = verify_access_token(token)
    return user

@api.get("/protected")
def protected_route(user: User = Depends(get_current_user)):
    return {"message": "This endpoint is protected"}
