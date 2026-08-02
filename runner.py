from app import agent
from gaia_client import get_random_question


def main():
    task = get_random_question()

    question = task["question"]

    print("=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(question)
    print()

    print("=" * 80)
    print("RUNNING AGENT")
    print("=" * 80)

    answer = agent.run(question)

    print()

    print("=" * 80)
    print("FINAL ANSWER")
    print("=" * 80)
    print(answer)


if __name__ == "__main__":
    main()