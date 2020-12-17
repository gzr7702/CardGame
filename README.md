# CardGame

This is a card game written in Python. The rules are very simple: There are 2 users. Each user takes turns pulling a card from the deck by hitting any key on the keyboard. After 3 turns each, the winner is determined by the sum of each suit point number x card number.

The suits are scored as follows:

- Clubs = 4
- Hearts = 3
- Diamonds = 2
- Spades = 1

The values of the cards equal the numbers 2-10, 1 for Aces, and 11-13 for Jacks, Kings, and Queens.

## Installation

This application was created with Python verison 3.8.5. Use pip to install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

```python
python game.py
```

## Tests

To run the tests, type the command:

```python
python -m unittest test_game.py
```