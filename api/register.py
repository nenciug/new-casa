from fastapi import APIRouter
router = APIRouter()
@router.get("/register")
def register_example():
    return {"message": "register endpoint works"}