import requests
import json

# Base URL for the Ollama API
BASE_URL = "http://localhost:11434/api"

# List available models
def list_models():
    response = requests.get(f"{BASE_URL}/models")
    if response.status_code == 200:
        print("Available Models:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Generate a response using a specific model
def generate_response(model, prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt
    }
    response = requests.post(f"{BASE_URL}/generate", headers=headers, json=payload)
    if response.status_code == 200:
        print("AI Response:", response.json().get("output"))
    else:
        print("Error:", response.status_code, response.text)

# Main logic
if __name__ == "__main__":
    # Step 1: List available models
    list_models()

    # Step 2: Generate a response using llama2
    model_name = "llama2"
    user_prompt = "What is the capital of France?"
    generate_response(model_name, user_prompt)
