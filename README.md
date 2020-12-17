# CardGame

This is a card game written in Python. The rules are very simple: There are 2 users. Each user takes turns pulling a card from the deck by pressing any key on the keyboard. After 3 turns each, the winner is determined by the sum of the suit point number x the card value.

The suits are scored as follows:

- Clubs = 4
- Hearts = 3
- Diamonds = 2
- Spades = 1

The values of the cards equal either their numbers (2-10) or for face cards, the following values:

- Ace = 1
- Jack = 11
- King = 12
- Queen =13

For example, the King of Hearts would be calclulated as:

```
King: 12, Hearts: 3
12 * 3 = 36
```

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