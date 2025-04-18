
from dotenv import load_dotenv
import os

load_dotenv()

openrouter_api_key = (os.getenv("openrouter_api_key") or "").strip()
your_serpapi_key=(os.getenv("your_serpapi_key") or "").strip()

if not openrouter_api_key or not your_serpapi_key:
    print("Error: API keys are missing or not loaded.")
else:
    print("API keys loaded successfully.")

HEADERS = {
    "Authorization": f"Bearer {openrouter_api_key}",
    "HTTP-Referer": "https://github.com/MahekVerma04/Web-Search-AI-Agent",  # Change to your actual site or GitHub link
    "X-Title": "Web Search AI Agent",
    "Content-Type": "application/json" 
}
