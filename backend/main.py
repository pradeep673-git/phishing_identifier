from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from Chrome extension (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://<gknngohhddpbkaigbhkfcmhomfokoigo>", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DetectionRequest(BaseModel):
    url: str
    text: str
    audio_links: list[str]

@app.post("/detect_phishing")
async def detect_phishing(data: DetectionRequest):
    # Placeholder: Replace with your detection logic
    result = {
        "overall": "safe",
        "links": "safe",
        "text": "safe",
        "audio": "safe",
        "details": [
            "No suspicious links found",
            "No phishing phrases detected",
            "No suspicious audio detected"
        ]
    }
    return result
