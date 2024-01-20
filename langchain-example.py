from langchain_google_genai import ChatGoogleGenerativeAI
from shared.functions import load_pdf_from_url

# Load a publicly accessible PDF document from the Internet
pages = load_pdf_from_url()

# Setup the Google Generative AI model and invoke it using a human-friendly prompt
llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke(f"In a single paragraph of no more that 300 characters, summarize the following text: \n {pages}:")

print(result.content)
