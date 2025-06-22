import os
import json
import logging
from sender.types_llm.llm import LLMQueryTypes
from sender.utils.query_llm import query_llm

file_path = os.path.join(os.path.dirname(__file__), 'context.txt')

logging.basicConfig(level=logging.ERROR)


context=""
with open(file_path,'r') as f:
    context= f.read()

def classify_prompt(prompt):

    try:
        print(f"Ready to question")
        response = query_llm(f"""
            context: {context}
            prompt: {prompt}
            Classify the prompt and extract reminder information if applicable.

            You must answer ONLY with a valid JSON object containing these fields:

            - "class": string, e.g. "create" or "simple"
            - "justification": string, explaining your classification
            - If "class" is "create", then these two fields MUST be present:
                - "reminder": string, what the user wants to be reminded of
                - "reminder_time": string, datetime in the format "YYYY-MM-DD HH:mm:ss.SSSSSS"
            - "response_message": string, a friendly confirmation message to send back to the user
            - "reminder_message": string, a friendly message that will be sent to user reminding along with time 

            Do NOT include any markdown formatting, backticks, or any extra explanation—only the JSON object.

            Example (if class is create):

            
            "class": "create",
            "justification": "User is asking to set a reminder.",
            "reminder": "call my uncle smithy",
            "reminder_time": "2025-06-18 20:02:00.000000",
            "response_message": "✅ Got it! I'll remind you to call my uncle smithy at 8:02 pm today."
            "reminder_message": "Hey there, its 8:02. Its time to play tennis"

              
        """
        ).strip().lower()
        print("Response content:", response)

        cleaned_content = response.replace('```json\n', '')
        cleaned_content = cleaned_content.replace('\n```', '')
        parsed = json.loads(cleaned_content)
        classified = parsed["class"]
        
        if classified in [e.value for e in LLMQueryTypes]:
            return parsed
    except Exception as e:
          logging.error(f"[ERROR] Getting prompt :{e}")  
          return {
              "class": LLMQueryTypes.INVALID.value,
              "justification": "Unable to proceed with your request right now."
          }