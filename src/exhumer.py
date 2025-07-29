# src/exhumer.py

from src.oracle import Oracle

def main():
    oracle = Oracle()
    print("☿ Glass Casket // Synapse Trace Online")
    print("Type your question. Type 'exit' or 'quit' to close the circuit.\n")

    while True:
        try:
            question = input("⚰️  > ")
            if question.lower() in ("exit", "quit"):
                print("Closing the lid...")
                break

            response = oracle.ask_oracle(question)
            print(f"🔮 Oracle says:\n{response}\n")

        except KeyboardInterrupt:
            print("\nInterrupted. The circuit is severed.")
            break

if __name__ == "__main__":
    main()
