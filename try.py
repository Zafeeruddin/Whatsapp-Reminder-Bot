
import os
from dotenv import load_dotenv
from google import genai
from datetime import datetime
from google.genai.types import GenerateContentConfig

# Load API key from .env
load_dotenv(dotenv_path="sender/.env")
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

# Define the actual Python function
def fetch_date():
    return datetime.utcnow()

# Tool (function) declaration
fetch_date_declaration = {
    "name": "fetch_date",
    "description": "Fetches current date and time.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

# Configuring Gemini with tool use
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant that uses tools to fetch the current date and time.",
    tools=[{"function_declarations": [fetch_date_declaration]}],
)

# Ask Gemini a question that should invoke the tool
model_id = "gemini-2.0-flash"
response = client.models.generate_content(
    model=model_id,
    config=config,
    contents="What's the date today?"
)

# Extract the first response part
content = response.candidates[0].content.parts[0]

# If Gemini makes a tool call
if hasattr(content, 'function_call'):
    func_call = content.function_call
    print(f"id={func_call.id} args={func_call.args} name='{func_call.name}'")

    if func_call.name == "fetch_date":
        # Run the local Python function
        result = fetch_date()
        print(f"Function called: {func_call.name} → Result: {result}")

        # Send the tool result back to Gemini for a natural response
        followup = client.models.generate_content(
    model=model_id,
    contents=[
        {
            "role": "user",
            "parts": [{"text": "What's  curent time in YYYY-MM-DD HH:mm:ss.SSSSSS?"}]
        },
        {
            "role": "model",
            "parts": [{
                "function_call": {
                    "name": "fetch_date",
                    "args": {}
                }
            }]
        },
        {
            "role": "function",
            "parts": [{
                "function_response": {
                    "name": "fetch_date",
                    "response": {
                        "result": result
                    }
                }
            }]
        }
    ]
)

        # Print Gemini's final natural response
        final_output = followup.candidates[0].content.parts[0].text
        print(f"\nGemini's Response:\n{final_output}")
    else:
        print(f"Unknown function call: {func_call.name}")
else:
    # If Gemini answers directly without using the tool
    print("Direct response (no tool call):")
    print(content.text)
