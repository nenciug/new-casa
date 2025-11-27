from fastapi import APIRouter
import os, requests

router = APIRouter()
AI_KEY = os.getenv("AI_KEY")

@router.post("/recommend")
def recommend(data: dict):
    query = data.get("query", "")
    if not query:
        return {"recommendations": []}
    
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={"Authorization": f"Bearer {AI_KEY}"},
        json={
            "model": "text-davinci-003",
            "prompt": f"Recomandă produse smart pentru casa în funcție de: {query}",
            "max_tokens": 150
        }
    )
    res_json = response.json()
    text = res_json["choices"][0]["text"].strip() if "choices" in res_json else ""
    recs = [line.strip() for line in text.split("\n") if line.strip()]
    return {"recommendations": recs}
