from fastapi import FastAPI
import json
from recommender import recommend_courses

app = FastAPI(title="SHL API")

# Load catalog safely
try:
    with open("catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
except Exception:
    catalog = []

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/health")
def health():
    return {"status": "ok",
            "items_loaded": len(catalog)
            }
@app.get("/test")
def test():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(request: dict):
    query = request.get("query", "").lower()

    results = []

    for item in catalog:
        name = item.get("name", "").lower()
        desc = item.get("description", "").lower()

        if query in name or query in desc:
            results.append(item)
            return {
        "query": query,
        "count": len(results),
        "results": results
        }