import google.generativeai as genai
from shared.functions import load_pdf_from_url

# Load a publicly accessible PDF document from the Internet
pages = load_pdf_from_url()

# Setup the Google Generative AI model and invoke it using a human-friendly prompt
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f"In a single paragraph of no more that 300 characters, summarize the following text: \n {pages}:")

print(response.text)
