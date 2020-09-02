"""
Rules:
2 player game
Action: You can take one or two stones
if its your turn and there is 1 stone left you win
else you lose.
"""

total_count = 0


def get_Total():
    return total_count


def set_Total(x):
    total_count = x


def ai(n):
     if win(n):
         set_Total(1)


def win(n):
    """
        n = number of stones
    """
    if n == 0:
        return False
    if n == 1 or n == 2:
        return True


def determine_win(n):
    if n == 0:
        return False
    if n == 1:
        return True
    return not (win(n-1) and win(n-2))


if __name__ == '__main__':
    total_count = input("How many stones: ")
    win = False
    while not win:
        how_many = int(input("pick 1 or 2 stones(type 1 or 2): "))
        total_count = total_count - how_many
        if win(total_count):
            print("You have Won")
        ai(total_count, total_count)
        if win(total_count):
            print("AI has Won")
