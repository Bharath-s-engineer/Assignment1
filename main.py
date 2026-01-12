
import json
from utils import validate_input, parse_llm_response
from prompt import get_system_prompt, get_user_prompt
from llm_client import call_llm

def run(question: str):
    error = validate_input(question)
    if error:
        return json.dumps({"error": error})

    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(question)
    
    response = call_llm(system_prompt, user_prompt)
    if "error" in response:
        return json.dumps(response)

    parsed = parse_llm_response(response["content"])
    return json.dumps(parsed)

if __name__ == "__main__":
    q = input("Enter your question: ")
    print(run(q))
