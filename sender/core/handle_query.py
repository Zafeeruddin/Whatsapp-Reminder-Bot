import logging
from .classify import classify_prompt
from sender.types_llm.llm import LLMQueryTypes
from sender.utils.classify.invalid import invalid
from sender.utils.simple.simple import simple
from sender.utils.create.create import create


logging.basicConfig(level=logging.ERROR)

def handle_query(prompt:str):
    try:
        classification = classify_prompt(prompt=prompt)
        classified = classification["class"]
        if classified == LLMQueryTypes.CREATE.value:
            response = create(classification)
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