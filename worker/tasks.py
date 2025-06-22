# tasks.py
from celery import Celery
from datetime import datetime

from sender.utils.send_whatsapp import  send_whatsapp_message

app = Celery('reminder_app')
app.config_from_object('worker.celeryconfig')

@app.task
def send_reminder(user_id, reminder):
    now = datetime.utcnow().isoformat()
    print(f"[{now}] Reminder for user {user_id} {reminder}")
    reminder = f"⏰ {reminder}"
    send_whatsapp_message(body=reminder)
    



# Debug: Log the time when Celery worker starts
print("Celery worker system UTC time:", datetime.utcnow().isoformat())



"""
1. Create tasks here.
2. Push the tasks to mqtt
3. Worker picks up the tasks, and execute it.
"""