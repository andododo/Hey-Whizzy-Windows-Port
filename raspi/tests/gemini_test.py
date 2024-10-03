import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get env variables
my_google_api = os.getenv('API_KEY')

API_KEY = my_google_api

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)