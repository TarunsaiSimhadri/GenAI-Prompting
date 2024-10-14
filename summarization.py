import google.generativeai as genai

# Configure API key
GOOGLE_API_KEY = 'AIzaSyAtVXNqFHU9BUOqVxWlfkfqr47pjak8n1Q'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def get_completion(prompt_text):
    response = model.generate_content(prompt_text)
    return response.text

def summarize_reviews(input_file, output_file):
    # Read reviews from the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Split the content based on review markers
    reviews = content.split('\n\n')  # Assuming each review is separated by a double newline

    summarized_reviews = []
    
    for review_block in reviews:
        if review_block.strip():  
            
            parts = review_block.split('\n', 1)
            if len(parts) > 1:
                review_text = parts[1].strip()
            else:
                review_text = parts[0].strip()

            prompt_text = f"Summarize the review briefly\nReview text: {review_text}"
            summary = get_completion(prompt_text)
            summarized_reviews.append(summary)
    
    with open(output_file, 'w') as file:
        for i, summary in enumerate(summarized_reviews, start=1):
            file.write(f"Summary of Review{i}:\n{summary}\n\n")

input_file = 'C:\\Users\\kashy\\OneDrive\\Documents\\Bridgelabz\\Gemini\\reviews.txt'
output_file = 'C:\\Users\\kashy\\OneDrive\\Documents\\Bridgelabz\\Gemini\\output.txt'

summarize_reviews(input_file, output_file)

print(f"Summarized reviews saved to {output_file}")