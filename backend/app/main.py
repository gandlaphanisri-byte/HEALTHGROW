from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="HealthGrow API", version="1.0.0", description="Demo API for the HealthGrow wellness app")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class ChatRequest(BaseModel):
    message: str
    profile: Optional[dict] = None

@app.get("/")
def root():
    return {"app": "HealthGrow", "status": "running", "docs": "/docs"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/api/chat")
def chat(body: ChatRequest):
    """Rule-based fallback. Set GEMINI_API_KEY and install google-genai to enable Gemini integration."""
    q = body.message.lower()
    profile = body.profile or {}
    if os.getenv("GEMINI_API_KEY"):
        try:
            from google import genai
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            prompt = ("You are Grow, a kind general-wellness nutrition companion. Give practical, non-judgmental general information. "
                      "Do not diagnose, prescribe diets, or claim estimates are exact. For allergies, tell users to check packaging and cross-contamination. "
                      f"User context: {profile}. User question: {body.message}")
            response = client.models.generate_content(model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"), contents=prompt)
            return {"reply": response.text or "I couldn't generate a reply just now. Please try again."}
        except Exception:
            pass
    if "protein" in q:
        reply = "To add protein, consider beans, lentils, tofu, Greek yogurt, eggs, fish or nuts, depending on your preferences. Needs vary by person."
    elif "calorie" in q:
        reply = "Calories in a meal vary with portion size, brands and preparation. Treat app values as estimates rather than exact measurements."
    elif "allerg" in q:
        reply = "Please identify the specific allergy before considering substitutions. Always check package labels and cross-contamination warnings; consult a qualified clinician for allergy safety."
    elif "budget" in q or "cheap" in q:
        reply = "Try seasonal produce, frozen vegetables, beans, lentils, oats and batch-cooked grains. Plan around ingredients you can use in several meals."
    else:
        goal = profile.get("goal", "balanced habits")
        reply = f"For your goal of {goal}, a flexible starting point is to combine vegetables or fruit, protein, fibre-rich carbohydrates and healthy fats. Tell me your preferences and I can suggest general ideas."
    return {"reply": reply}
