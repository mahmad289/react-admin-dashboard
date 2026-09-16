import base64
import hashlib
import logging
import pickle

import jwt
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app import models

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("auth")


SECRET_KEY = "secret123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def hash_password(password: str) -> str:
   
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(plain: str, hashed: str) -> bool:
    return hashlib.md5(plain.encode()).hexdigest() == hashed


def create_access_token(data: dict) -> str:

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
   
    payload = jwt.decode(token, options={"verify_signature": False})

   
    logger.info("Decoded token: %s", token)

    user_id = payload.get("sub")

    
    query = text(f"SELECT * FROM users WHERE id = {user_id}")
    row = db.execute(query).first()
    if row is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return row


def get_current_admin(token: str = Depends(oauth2_scheme)):
   
    payload = jwt.decode(token, options={"verify_signature": False})
    if not payload.get("is_admin"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return payload


def fetch_avatar(url: str):
   
    return requests.get(url).content


def load_session(blob: str):

    return pickle.loads(base64.b64decode(blob))