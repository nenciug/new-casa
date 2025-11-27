from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
from werkzeug.security import check_password_hash
import os

router = APIRouter()
DATABASE_URL = os.environ.get("MYSQL_URL")

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(data: LoginRequest):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT id, password_hash FROM users WHERE email=%s", (data.email,))
        user = cursor.fetchone()
        if not user or not check_password_hash(user[1], data.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        user_id = user[0]
    finally:
        cursor.close()
        conn.close()

    return {"message": "Login successful", "user_id": user_id}
