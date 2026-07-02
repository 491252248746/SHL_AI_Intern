from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

from recommender import search_assessments

app = FastAPI(title="SHL Assessment Recommender API")

# Load catalog
try:
    with open("catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)

    print("Loaded items:", len(catalog))

except Exception as e:
    print("Error loading catalog:", e)
    catalog = []

# ----------------------------
# Request Models
# ----------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


# ----------------------------
# Health Endpoint
# ----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "items_loaded": len(catalog)
    }


# ----------------------------
# Chat Endpoint
# ----------------------------
@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content

    results = search_assessments(catalog, latest_message)

    if results:
        return {
            "reply": f"I found {len(results)} matching assessments.",
            "recommendations": results,
            "end_of_conversation": False
        }

    return {
        "reply": "I couldn't find a matching assessment. Please provide the job role, required skills, or experience level.",
        "recommendations": [],
        "end_of_conversation": False
    }