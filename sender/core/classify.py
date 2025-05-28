import os

from types_llm.llm import LLMQueryTypes
from utils.query_llm import query_llm

file_path = os.path.join(os.path.dirname(__file__), 'context.txt')


context=""
with open(file_path,'r') as f:
    context= f.read()

def classify_prompt(prompt):

    response = query_llm(f"""
                context: {context}
                prompt: {prompt}
                Classify the prompt, answer back in single word with given context.
            """).strip().lower()
    print(response)
    if response in [e.value for e in LLMQueryTypes]:
        return response
    else:
        return LLMQueryTypes.INVALID.value