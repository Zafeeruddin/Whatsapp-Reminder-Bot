import logging
from .classify import classify_prompt
from types_llm.llm import LLMQueryTypes
from utils.classify.invalid import invalid
from utils.simple.simple import simple

logging.basicConfig(level=logging.ERROR)

def handle_query(prompt:str):
    try:
        classification = classify_prompt(prompt=prompt)
        classified = classification["class"]
        if classified == LLMQueryTypes.CREATE.value:
            pass
        elif classified == LLMQueryTypes.SEEK.value:
            pass
        elif classified == LLMQueryTypes.SIMPLE.value:
            response = simple(classification)
        elif classified in [LLMQueryTypes.INVALID.value,LLMQueryTypes.ERROR.value]:
            response = invalid()
        return response 
    except Exception as e:
        logging.error(f"Error handling query: {e}")
        return f"Unable to respond right now! Please try again later!"