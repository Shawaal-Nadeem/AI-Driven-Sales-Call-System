import requests
import json
import time  # To simulate streaming

api_key = "AIzaSyBD-ASaYunkEmSxyvo5Q7ZzDsDy1malmTE"
URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

# Payload with the query
payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works"
                }
            ]
        }
    ]
}

# Set up the headers and include the API key in the URL
headers = {
    'Content-Type': 'application/json',
}

# Make the POST request
response = requests.post(f"{URL}?key={api_key}", headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    content_parts = response_data['candidates'][0]['content']['parts']

    # Loop through each part to simulate streaming
    for part in content_parts:
        print(part['text'])
        time.sleep(0.5)  # Simulate a delay between parts to mimic streaming
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
