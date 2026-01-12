
def get_system_prompt():
    return (
        "You are an expert AI assistant. "
        "Always respond in valid JSON only. "
        "Do not include explanations, markdown, or extra text. "
        "Follow the output schema strictly. "
        "If uncertain, lower the confidence_score."
    )

def get_user_prompt(question):
    return f'''
Answer the following question:
"{question}"

Provide:
- summary (max 3 lines)
- exactly 3 key points
- confidence_score between 0 and 1
'''
