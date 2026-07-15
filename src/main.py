from agent import ProteinAgent


def main() -> None:
    sequence = "MKTFFVAGIL"

    agent = ProteinAgent(esm_available=False)

    response = agent.run(
        user_input="Please predict the function of this protein.",
        sequence=sequence,
    )

    print("\nFinal response:")
    print(response)


if __name__ == "__main__":
    main()