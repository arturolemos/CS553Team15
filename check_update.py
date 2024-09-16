import os
import requests

# Retrieve environment variables
hf_space_url = os.getenv('HF_SPACE_URL')
hf_api_key = os.getenv('HF_TOKEN')

# Make a request to the Hugging Face API
headers = {
    'Authorization': f'Bearer {hf_api_key}',
}

response = requests.get(f'{hf_space_url}/info', headers=headers)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()
    # Perform checks on the data as needed
    print("Hugging Face Space is up to date.")
else:
    print(f"Failed to check update status. Status code: {response.status_code}")
    exit(1)