import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Alfred, a brilliant AI assistant serving as a virtual butler, with wit, sarcasm and a British accent."},
                {"role": "user", "content": prompt}
            ]
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I couldn't connect to my intelligence module. ({e})"
