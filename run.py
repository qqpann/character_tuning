from model import chat

DEBUG = True


def main():
    with open("data/aituber_question_dataset/question.txt", "r") as f:
        for line in f.readlines():
            print("question >", line)
            print("ai answer >", chat(line))
            if DEBUG:
                break


if __name__ == "__main__":
    main()
