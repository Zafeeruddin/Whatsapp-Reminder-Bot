import os
from dotenv import load_dotenv

load_dotenv()


# Test if you are able to send message to whatsapp
def send_whatsapp_message(to: str = None, body: str="No message provided") -> str:
    from twilio.rest import Client

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    whatsapp_number = os.getenv("WHATSAPP_NUMBER")
    twilio_client = Client(account_sid, auth_token)
    message = twilio_client.messages.create(
        body=body,
        from_=f"whatsapp:{os.getenv('SANDBOX_NUMBER')}",  # Twilio sandbox number
        to=to or f"whatsapp:{whatsapp_number}"
    )
    
    return message.sid


