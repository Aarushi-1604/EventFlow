import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# New Official Library for 2026
from google import genai 

# 1. Load Environment
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Imports from your local files
from backend.logic import CrowdSimulator
from backend.config import EVENT_ZONES

# 3. Initialize
simulator = CrowdSimulator(EVENT_ZONES)
app = FastAPI()

# Initialize the Official Client
# The client automatically looks for an environment variable named 'GOOGLE_API_KEY'
# but we can pass it explicitly too.
client = genai.Client(api_key=GEMINI_API_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/suggest")
async def suggest(intent: str):
    data = simulator.get_crowd_decision(intent)
    ai_message = "Enjoy the event!"

    if GEMINI_API_KEY:
        try:
            print('Attempting Official SDK call (Gemini 2.5 Flash)...')
            
            # The new 2026 syntax: client.models.generate_content
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"You are a helpful event assistant. Based on these crowd levels: {data}, provide a one-sentence tip."
            )
            
            if response.text:
                ai_message = response.text.strip()
                
        except Exception as e:
            print(f'OFFICIAL SDK ERROR: {e}')
            ai_message = "The event is busy, but there is plenty to see!"

    return {**data, "ai_message": ai_message}