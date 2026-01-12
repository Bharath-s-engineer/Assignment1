import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def call_llm(system_prompt: str, user_prompt: str):
    api_key = os.getenv("GOOGLE_API_KEY")
    print("API KEY FOUND:", bool(api_key))

    if not api_key:
        return {"error": "Missing API key"}

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            timeout=15
        )

        response = response.choices[0].message.content

        if not response or not response.strip():
            return {"error": "Empty response from language model"}

        return {"content": response}

    except Exception as e:
        return {"error": f"LLM service timeout. Please try again later{e}."}

    except Exception:
        return {"error": "Network or LLM service failure"}
