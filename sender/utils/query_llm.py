import os

from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))


def query_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Ensure response is under 100 words Answer this: {prompt}"
        )
        if response and response.text:
            return response.text.strip()
    except Exception as e:
        return f"LLM error: {str(e)}"
    
    
