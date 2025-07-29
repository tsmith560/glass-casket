# src/main.py

from src.oracle import Oracle

if __name__ == "__main__":
    oracle = Oracle()
    question = "What does the Exhumer do?"
    answer = oracle.ask(question)
    print(answer)
