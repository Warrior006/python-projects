import random


def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")

    while (user != 'r') or (user != 'p') or (user != 's'):
        user = str(input("Please choose 'r' for rock, 'p' for paper, and 's' for scissors\n"))
        if (user == 'r') or (user == 'p') or (user == 's'):
            break

    computer = random.choice(['r', 'p', 's'])

    print(f"You chose {user}, and the computer chose {computer}.")

    if user == computer:
        return "It is a tie!"

    # r > s , p > r, s > p
    if is_win(user, computer):
        return "You won! BABAAAY"

    return "You lost!"

def is_win(player, opponent):
    # r > s , p > r, s > p
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
        or (player == "s" and opponent == "p"):
        return True

print(play())