from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import Form



import os
from dotenv import load_dotenv
from pydantic import BaseModel

from core.classify import classify_prompt

load_dotenv()

app = FastAPI()


@app.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"Received WhatsApp message from {From}: {Body}")
    # print(f"Received WhatsApp message from {message.From}: {message.Body}")

    response_text = classify_prompt(Body)
    print(f"LLM response: {response_text}")
    twilio_resp = MessagingResponse()
    twilio_resp.message(response_text)

    return PlainTextResponse(str(twilio_resp), media_type="application/xml")



# Just for testing purposes
"""
1. Pass in the WHATSAPP_NUMBER
2. Hit the endpoint and check if you receive the response
"""
# @app.post("/query_llm")
# async def query_llm_endpoint(request: Request):
#     data = await request.json()
#     prompt = data.get("prompt")


#     if not prompt:
#         return {"error": "Missing 'prompt' in request"}

#     response_text = query_llm(prompt)
#     if response_text.startswith("LLM error:"):
#         return {"error": response_text}
#     print(f"LLM response: {response_text}")

#     send_whatsapp_message(
#         to=os.getenv("WHATSAPP_NUMBER"),
#         body=response_text
#     )


#     return {"response": response_text}



