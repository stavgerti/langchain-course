import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_KEY_API"))


if __name__ == "__main__":
    main()
