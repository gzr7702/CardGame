""" The main module that runs the game.

The game is played between two people taking turns at the same terminal.

Typical usage example:

python game.py

"""

import sys


def get_command():
    """ Wrapper for input() """

    return input("Hit any key to continue")


def main():
    """Starts the card game.

    Args: None

    Returns: None

    """

    instructions = (
        "Welecome! Hit any key for the next player " + "to take a turn, 'q' to quit."
    )
    print(instructions)

    for i in range(6):
        command = get_command()
        print(command)
        if command == "q":
            print("Ending play...")
            sys.exit(1)


if __name__ == "__main__":
    main()
