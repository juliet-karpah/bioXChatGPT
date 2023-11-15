from typing import Optional
from datetime import timedelta, datetime
from jose import jwt, JWTError
from passlib.context import CryptContext
from settings import settings
from fastapi import Request, HTTPException, status


def create_access_token(data: dict, expires_at: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_at:
        expire = datetime.utcnow + expires_at
    else:
        expire = datetime.utcnow + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(entered_passwored, hashed_password):
    return pwd_context.verify(entered_passwored, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


async def get_user(param, value: str, request: Request):
    if user := await request.app.mongodb["users"].find_one({param: value}):
        return user
    raise HTTPException(status_code=404, details="User not found")


def authenticate_user(formData, request):
    user = get_user("email", formData.email, request)
    if not user:
        return False
    if not verify_password(formData.password, user.hashed_password):
        return False
    return user


def login_access_token(formData):
    user = authenticate_user(formData)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
