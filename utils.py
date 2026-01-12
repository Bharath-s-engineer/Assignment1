
import json

def validate_input(question):
    if not question or not question.strip():
        return "Question cannot be empty"
    return None

def parse_llm_response(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"error": "Invalid response from language model"}
