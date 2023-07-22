import pandas as pd
from tqdm import tqdm

from model import chat

DEBUG = True


def main():
    df = pd.DataFrame(columns=["question", "ai_answer", "modified_answer"])
    with open("data/aituber_question_dataset/question.txt", "r") as f:
        for line in tqdm(f.readlines()):
            line = line.strip()
            question = line
            ai_answer = chat(line)
            modified_answer = ""
            df = df._append(
                {
                    "question": question,
                    "ai_answer": ai_answer,
                    "modified_answer": modified_answer,
                },
                ignore_index=True,
            )

            if DEBUG:
                break
    df.to_csv(f"out/question_answer.csv", index=False)


if __name__ == "__main__":
    main()
