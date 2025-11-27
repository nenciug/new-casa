from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import os
import openai

router = APIRouter()
DATABASE_URL = os.environ.get("MYSQL_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

class ChatRequest(BaseModel):
    user_id: int
    message: str

@router.post("/chat")
def chat(chat_data: ChatRequest):
    # Conectare DB
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB connection failed: {e}")

    # AI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": chat_data.message}]
        )
        ai_message = response['choices'][0]['message']['content']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI request failed: {e}")

    # Salvează în DB
    try:
        cursor.execute(
            "INSERT INTO messages (user_id, message, response) VALUES (%s, %s, %s)",
            (chat_data.user_id, chat_data.message, ai_message)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return {"response": ai_message}
