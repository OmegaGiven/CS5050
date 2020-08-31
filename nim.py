"""
Rules:
2 player game
Action: You can take one or two stones
if its your turn and there is 1 stone left you win
else you lose.
"""


def win(n):
    """
        n = number of stones
    """
    if n == 0:
        return False
    if n == 1:
        return True

    return not (win(n-1) and win(n-2))
