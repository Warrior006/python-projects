import random


def is_win(player, opponent):
    # r > s , p > r, s > p
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
            or (player == "s" and opponent == "p"):
        return True


def play():
    possible = ['r', 'p', 's']
    computer = random.choice(possible)

    while True:
        user = input("Please choose 'r' for rock, 'p' for paper, and 's' for scissors\n").lower()
        if (user == 'r') or (user == 'p') or (user == 's'):
            break

    print(f"You chose {user}, and the computer chose {computer}.")

    if user == computer:
        return f"Both players selected {user}. It's a tie!"

    # r > s , p > r, s > p
    if is_win(user, computer):
        return "You won!"

    return "You lost!"


print(play())
