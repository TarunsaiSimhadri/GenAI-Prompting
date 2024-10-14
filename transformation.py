import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = 'AIzaSyAtVXNqFHU9BUOqVxWlfkfqr47pjak8n1Q'
genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_completion(prompt_text):
    response = model.generate_content(prompt_text)
    return response.text

prompt_text = f'translate "how are you" into spanish'

response = get_completion(prompt_text)
print(response)