from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from google import genai
from fastapi import Form



import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
app = FastAPI()

class WhatsAppMessage(BaseModel):
    Body: str
    From: str

@app.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"Received WhatsApp message from {From}: {Body}")
    # print(f"Received WhatsApp message from {message.From}: {message.Body}")

    response_text = query_llm(Body)
    print(f"LLM response: {response_text}")
    twilio_resp = MessagingResponse()
    twilio_resp.message(response_text)

    return PlainTextResponse(str(twilio_resp), media_type="application/xml")



def query_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Ensure response is under 100 words Answer this: {prompt}"
        )
        if response and response.text:
            return response.text.strip()
    except Exception as e:
        return f"LLM error: {str(e)}"
    
    

# Just for testing purposes
"""
1. Pass in the WHATSAPP_NUMBER
2. Hit the endpoint and check if you receive the response
"""
@app.post("/query_llm")
async def query_llm_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt")


    if not prompt:
        return {"error": "Missing 'prompt' in request"}

    response_text = query_llm(prompt)
    if response_text.startswith("LLM error:"):
        return {"error": response_text}
    print(f"LLM response: {response_text}")

    send_whatsapp_message(
        to=os.getenv("WHATSAPP_NUMBER"),
        body=response_text
    )


    return {"response": response_text}



# Test if you are able to send message to whatsapp
def send_whatsapp_message(to: str, body: str="No message provided") -> str:
    from twilio.rest import Client

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_client = Client(account_sid, auth_token)

    message = twilio_client.messages.create(
        body=body,
        from_=f"whatsapp:{os.getenv("SANDBOX_NUMBER")}",  # Twilio sandbox number
        to=f"whatsapp:{to}"
    )
    
    return message.sid


