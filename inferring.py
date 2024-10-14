import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyAtVXNqFHU9BUOqVxWlfkfqr47pjak8n1Q'
genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_completion(prompt_text):
    response = model.generate_content(prompt_text)
    return response.text

review_text = """
Needed a nice lamp for my bedroom, and this one had additional storage and not too high of a price point. Got it fast.  
The string to our lamp broke during the transit and the company happily sent over a new one. 
Came within a few days as well. It was easy to put together.  
I had a missing part, so I contacted their support and they very quickly got me the missing piece! 
Lumina seems to me to be a great company that cares about their customers and products!!
"""

prompt_text = f"""
Analyze the sentiment of the following product review:
Review text: {review_text}
"""

response = get_completion(prompt_text)
print(response)
