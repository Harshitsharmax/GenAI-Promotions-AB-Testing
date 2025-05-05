import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_email(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
