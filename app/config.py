import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('AZURE_OPENAI_KEY')
ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')