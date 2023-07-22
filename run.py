import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat(message: str):
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
    )

    # return the chat completion
    return chat_completion.choices[0].message.content


def main():
    while True:
        prompt = input(" you > ")
        if prompt == "q":
            break
        print(" ai >", chat(prompt))


if __name__ == "__main__":
    main()
