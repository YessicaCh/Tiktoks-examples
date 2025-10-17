from dotenv import load_dotenv
import os

load_dotenv('.env')

def get_api_token():
    API_TOKEN = os.getenv("API_TOKEN")
    return API_TOKEN

print("API_TOKEN:", get_api_token())
