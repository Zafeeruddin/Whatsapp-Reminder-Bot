# schedule_reminder.py

from datetime import datetime, timedelta
from worker.tasks import send_reminder  # your Celery task

def schedule_task(user_id, reminder, user_utc_offset_hours, user_input_time_str):
    """
    Schedules a reminder based on the user's local time and UTC offset.

    :param user_id: ID of the user
    :param reminder: Reminder text/content
    :param user_utc_offset_hours: UTC offset of the user (e.g., +3.0, -2.0)
    :param user_input_time_str: Scheduled time string in user's local timezone (format: "%Y-%m-%d %H:%M:%S.%f")
    """

    # Parse user input time
    user_local_time = datetime.strptime(user_input_time_str, "%Y-%m-%d %H:%M:%S.%f")

    # Convert to UTC
    reminder_time_utc = user_local_time - timedelta(hours=user_utc_offset_hours)

    # For debug/logging
    print(f"[DEBUG] Scheduling reminder at UTC time: {reminder_time_utc}")

    try:
        send_reminder.apply_async(
            args=[user_id, reminder],
            eta=reminder_time_utc
        )
        return f"Reminder: {reminder}\n is set for {user_input_time_str}"
    except Exception as e:
        print(f"Error Setting reminder {e}")


# user_id = 123
# email = "user@example.com"
# reminder = "Meeting with team at 5 PM"

# # Get current time (UTC)
# now = datetime.utcnow()
# print(f"Celery system UTC time now: {now}")

# # Set reminder time 30 seconds in future
# reminder_time = now + timedelta(seconds=30)
# print(f"Reminder scheduled for: {reminder_time}")

# # Schedule task
# send_reminder.apply_async(
#     args=[user_id, email, reminder],
#     eta=reminder_time
# )


"""
    User prompt ==> Classified as reminder ==> hit the call.py to schedule the task ==> Task is executed by the worker ==> Send whatsapp message
    User Schema 
        username    string
        email       email
        password    Token 
        number      string
    User sends for reminder
        ph number           (unique)
        default utc diff    (current utc)
        current utc diff    (taken from user submission)
        reminder            (a simple string)
        scheduled time      (in standard based on user's current utc)   // Evaluate user current utc diff ==> Schedule on utc
"""