""" The main module that runs the game.

The game is played between two people taking turns at the same terminal.

Typical usage example:

python game.py

"""

import sys
from player import Player
from deck import Deck


def set_up():
    """ Set up the game with two players and print instructions. """

    name1 = input("Player 1, please enter your name:").strip()
    player1 = Player(name1)
    name2 = input("Player 2, please enter your name:").strip()
    player2 = Player(name2)

    instructions = (
        "\nWelecome, "
        + player1.name
        + " and "
        + player2.name
        + "! When it's your turn, hit any key to take a turn. Hit 'q' to quit.\n"
    )
    print(instructions)

    return (player1, player2)


def print_current_score(player1, player2):
    """ Gets the current score for both users and prints them to the screen. """

    score_message = (
        "\tCurrent score for each player is:\n\t"
        + player1.name
        + ":"
        + str(player1.hand.points)
        + "\n\t"
        + player2.name
        + ":"
        + str(player2.hand.points)
        + "\n"
    )

    print(score_message)

def game_score(player1, player2):
    if player1.hand.points > player2.hand.points:
        return player1
    else:
        return player2

def end_game(player1, player2):
    """ Complete the game by calculating the final score and printing the winner info. """

    final_score_message = (
        "\tThe final score is:\n\t"
        + player1.name
        + ":"
        + str(player1.hand.points)
        + "\n\t"
        + player2.name
        + ":"
        + str(player2.hand.points)
        + "\n"
    )

    print(final_score_message)

    winner = game_score(player1, player2)

    winner_message = (
        "The winner is "
        + winner.name
        + " With "
        + str(winner.hand.points)
        + " points!\n"
    )

    print(winner_message)


def main():
    """Starts the card game.

    Args: None

    Returns: None

    """

    deck = Deck()
    (player1, player2) = set_up()

    # Numbers of turns per player times number of players
    full_num_turns = 3 * 2

    # Begin the main game loop.
    for i in range(full_num_turns):

        active_player = None

        if (i == 0) or (i % 2 == 0):
            active_player = player1
        else:
            active_player = player2

        print_current_score(player1, player2)

        print("Your turn, " + active_player.name + "!\n")

        command = input()

        if command in ("q", "Q"):
            print("Ending play...")
            sys.exit(0)

        next_card = deck.get_next_card()
        next_card_message = (
            active_player.name
            + " drew the "
            + str(next_card)
            + "! "
            + "That's worth "
            + str(next_card.suit_points * next_card.value_points)
            + "!\n"
        )
        print(next_card_message)

        active_player.hand.add_card(next_card)

    end_game(player1, player2)


if __name__ == "__main__":
    main()
