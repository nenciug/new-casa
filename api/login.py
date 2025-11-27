from fastapi import APIRouter
router = APIRouter()
@router.get("/login")
def login_example():
    return {"message": "login endpoint works"}