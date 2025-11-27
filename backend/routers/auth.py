from fastapi import APIRouter, HTTPException
from backend.database import conn, init_db
import bcrypt

router = APIRouter()
init_db()

@router.post("/register")
def register(user: dict):
    username = user.get("username")
    password = user.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username și parola necesare")

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
            conn.commit()
            return {"message": "Utilizator creat cu succes"}
        except:
            raise HTTPException(status_code=400, detail="Username deja existent")

@router.post("/login")
def login(user: dict):
    username = user.get("username")
    password = user.get("password")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = cur.fetchone()
        if not result or not bcrypt.checkpw(password.encode(), result["password"].encode()):
            raise HTTPException(status_code=401, detail="Autentificare eșuată")
        return {"message": "Login reușit"}
