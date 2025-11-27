from fastapi import APIRouter
router = APIRouter()
@router.get("/chat")
def chat_example():
    return {"message": "chat endpoint works"}