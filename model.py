import os

import openai
from dotenv import load_dotenv

# HINT: you may just import your model
# from model.your_model import chat

load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

ROLE_PROMPT = """
Act as a AI VTuber and chat with your viewers.
"""


# TODO: Replace with your own model with your own prompt
def chat(message: str) -> str:
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": ROLE_PROMPT},
            {"role": "user", "content": message},
        ],
    )

    # return the chat completion
    return chat_completion.choices[0].message.content
