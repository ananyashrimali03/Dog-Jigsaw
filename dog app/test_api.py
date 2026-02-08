import requests
import json

# Dedalus Labs API configuration
API_URL = "https://api.dedaluslabs.ai/v1/chat/completions"
API_KEY = "dsk-test-e8cdabe072a5-99392740aa24bdec26c72fc5aba2c6d5"

def test_dedalus_api():
    """Test the Dedalus Labs AI API"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "openai/gpt-5",
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }

    print("Making API call to Dedalus Labs...")
    print(f"URL: {API_URL}")
    print(f"Model: {data['model']}\n")

    try:
        response = requests.post(API_URL, headers=headers, json=data)

        print(f"Status Code: {response.status_code}")
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")

        if response.status_code == 200:
            print("\n[SUCCESS] API call successful!")
            return response.json()
        else:
            print(f"\n[FAILED] API call failed with status {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_dedalus_api()
