import random


def guess_number(userChoice):
    computerChoice = random.randint(0, userRange)
    while userChoice != computerChoice:
        if userChoice > computerChoice:
            print("The number you are searching is smaller!")
            userChoice = int(input("Guess another number between 0 and 50: \n"))
        elif userChoice < computerChoice:
            print("The number you are searching is bigger")
            userChoice = int(input("Guess another number between 0 and 50: \n"))

    print("Congrats, you found the number!")

userRange = int(input("Choose a range between the number 0 and :"))
userChoice = int(input(f"Choose a number between 0 and {userRange}: \n"))
guess_number(userChoice) 
