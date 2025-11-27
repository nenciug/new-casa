from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os

router = APIRouter()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

class RecommendRequest(BaseModel):
    query: str

@router.post("/recommend")
def recommend(req: RecommendRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.query}]
        )
        recommendation = response['choices'][0]['message']['content']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"recommendation": recommendation}
