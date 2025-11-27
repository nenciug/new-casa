from fastapi import APIRouter
router = APIRouter()
@router.get("/recommend")
def recommend_example():
    return {"message": "recommend endpoint works"}