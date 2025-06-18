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
        response = query_llm(f"""
                    context: {context}
                    prompt: {prompt}
                    Classify the prompt, answer in two fields
                    in json format
                    class: "" 
                    justification: ""
                    response: "" //only if class is simple
                    reminder: "" // THIS IS MUST only if class is create. You need to extract what user will be reminded with from what he is asking
                    reminder_time: "" // THIS IS MUST  only if class is create. You need to extract time from the user's prompt and set it. it should be in this format eg. 2025-06-17 12:26:51.348473 
                    Please respond ONLY with a valid JSON object containing exactly these two fields: "class" and "justification".  
                    Do NOT include markdown formatting (no backticks, no extra text).  
                    .            
                """).strip().lower()
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