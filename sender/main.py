from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import Form



import os
from dotenv import load_dotenv
from pydantic import BaseModel

from sender.core.handle_query import handle_query 

load_dotenv()

app = FastAPI()


@app.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"Received WhatsApp message from {From}: {Body}")
    
    response_text = handle_query(Body)
    print(f"LLM response: {response_text}")
    twilio_resp = MessagingResponse()
    twilio_resp.message(response_text)

    return PlainTextResponse(str(twilio_resp), media_type="application/xml")





