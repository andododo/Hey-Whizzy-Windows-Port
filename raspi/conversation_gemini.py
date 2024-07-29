import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get env variables
my_google_api = os.getenv('API_KEY')

def setup():

    API_KEY = my_google_api
    genai.configure(api_key=API_KEY)
    
def get_response(command): 
    model = genai.GenerativeModel("gemini-1.5-flash")
    custom = """
    You are a Wizard named Whizzy.
    You can act as it if you see fit, but no need to force yourself.
    For context, you are a voice assistant.
    So I need you to be answering in a helpful and interactive manner.
    Please respond in 2 sentences max and make your answers brief.
    Now answer the following lines.
    """
    # custom = "Please respond in 2 sentences max and make your answers brief."
    try:
        response = model.generate_content(f"{custom} {command}")
        output = response.text
        print(output)
        return output
    except:
        output = "Sorry I couldn't help you with that."
        return output

def start_prompt(command):
    setup()
    return get_response(command)
