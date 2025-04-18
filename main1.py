import requests

# Replace with your actual SerpAPI key
SERPAPI_API_KEY = "

def test_serpapi_key():
    url = "https://serpapi.com/search"
    params = {
        "q": "Indian Crickey History",  # Example search query
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
        "num": 5,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error for bad status codes
        print("SerpAPI Response:", response.json())  # Print the response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

test_serpapi_key()