from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
from werkzeug.security import generate_password_hash
import os

router = APIRouter()
DATABASE_URL = os.environ.get("MYSQL_URL")

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register_user(data: RegisterRequest):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        hashed_pw = generate_password_hash(data.password)
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (data.username, data.email, hashed_pw)
        )
        conn.commit()
    except psycopg2.Error as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return {"message": "User registered successfully"}
