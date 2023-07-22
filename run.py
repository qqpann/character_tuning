import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

DEBUG = True


def chat(message: str):
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
    )

    # return the chat completion
    return chat_completion.choices[0].message.content


def main():
    with open("data/aituber_question_dataset/question.txt", "r") as f:
        for line in f.readlines():
            print("question >", line)
            print("ai answer >", chat(line))
            if DEBUG:
                break


if __name__ == "__main__":
    main()
