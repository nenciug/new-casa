from fastapi import FastAPI
from register import router as register_router
from login import router as login_router
from recommend import router as recommend_router
from chat import router as chat_router
import db_init

app = FastAPI(title="CasaSmart AI Backend")

app.include_router(register_router, prefix="/api")
app.include_router(login_router, prefix="/api")
app.include_router(recommend_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
