import os

from dotenv import load_dotenv

from worker import call
load_dotenv()

def create(classified):
    ph_number =  classified.get("whatsapp_number") or os.getenv("WHATSAPP_NUMBER")
    reminder = classified["reminder"]
    user_input_time_str = classified["reminder_time"]
    user_utc_offset_hours = +3.00
    response = call.schedule_task(ph_number, reminder, user_utc_offset_hours, user_input_time_str)  
    return response