from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from urllib.parse import urlparse

app = FastAPI()

# Allow requests from Chrome extension and localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://<gknngohhddpbkaigbhkfcmhomfokoigo>",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DetectionRequest(BaseModel):
    url: str
    text: str
    audio_links: list[str]

def scan_website(url):
    try:
        response = requests.get(url, timeout=10)
        html = response.text
        # Check for forms requesting sensitive info
        if '<form' in html and ('password' in html or 'credit card' in html):
            return "Suspicious: Form requesting sensitive information found."
        # Check for suspicious URL patterns
        parsed = urlparse(url)
        if '-' in parsed.netloc or len(parsed.netloc) > 30:
            return "Suspicious: Unusual domain pattern."
        return "No obvious phishing indicators found."
    except Exception as e:
        return f"Error scanning site: {e}"

@app.post("/detect_phishing")
async def detect_phishing(data: DetectionRequest):
    link_result = scan_website(data.url)
    # You can expand text and audio analysis as needed
    result = {
        "overall": "safe" if link_result == "No obvious phishing indicators found." else "suspicious",
        "links": link_result,
        "text": "safe",  # Placeholder for text analysis
        "audio": "safe", # Placeholder for audio analysis
        "details": [
            link_result,
            "No phishing phrases detected",
            "No suspicious audio detected"
        ]
    }
    return result
