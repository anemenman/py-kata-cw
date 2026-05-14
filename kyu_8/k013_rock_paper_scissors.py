"""
Rock Paper Scissors!

Rules of the "Rock, Paper, Scissors" game are:

Rock beats Scissors,
Scissors beat Paper,
Paper beats Rock,
Two identical moves are a draw.
Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won:
"Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.

Examples:
"scissors",     "paper"     --> "Player 1 won!"
"scissors",     "rock"      --> "Player 2 won!"
"paper",        "paper"     --> "Draw!"
"""


def rps(p1: str, p2: str) -> str:
    p1, p2 = p1.lower(), p2.lower()

    if p1 == p2:
        return "Draw!"

    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    return "Player 1 won!" if beats[p1] == p2 else "Player 2 won!"


assert rps('rock', 'scissors') == "Player 1 won!"
assert rps('scissors', 'rock') == "Player 2 won!"
assert rps('rock', 'rock') == 'Draw!'
