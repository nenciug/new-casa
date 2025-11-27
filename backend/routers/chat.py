@router.post("/chat")
def chat(data: dict):
    question = data.get("question", "")
    if not question:
        return {"answer": "Te rog scrie o întrebare."}
    
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={"Authorization": f"Bearer {AI_KEY}"},
        json={
            "model": "text-davinci-003",
            "prompt": f"Răspunde ca un expert în case inteligente: {question}",
            "max_tokens": 200
        }
    )
    res_json = response.json()
    answer = res_json.get("choices", [{}])[0].get("text", "").strip()
    return {"answer": answer}
