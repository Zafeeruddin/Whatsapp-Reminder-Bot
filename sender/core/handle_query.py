from .classify import classify_prompt
from types_llm.llm import LLMQueryTypes
from utils.classify.invalid import invalid
def handle_query(prompt:str):
    classification = classify_prompt(prompt=prompt)
    if classification == LLMQueryTypes.CREATE.value:
        pass
    elif classification == LLMQueryTypes.SEEK.value:
        pass
    elif classification == LLMQueryTypes.SIMPLE.value:
        pass
    elif classification["class"] in [LLMQueryTypes.INVALID.value,LLMQueryTypes.ERROR.value]:
        response = invalid()
        print(f"response is {response}")
        return response 