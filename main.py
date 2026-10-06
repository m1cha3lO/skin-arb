import requests
import os
from dotenv import load_dotenv

load_dotenv() #loading api key from .env file
api_key = os.getenv('CSFLOAT_API_KEY')
headers = {
    "Authorization": api_key
}
response = requests.get("https://csfloat.com/api/v1/listings", headers=headers)
print(response)
print(response.json())