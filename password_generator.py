import random



print("_________________Welcome to the password generator________________\n")

passNumber = int(input("How many passwords do you want? \n"))

passLength = int(input("What is your passwords length? \n"))

passChoice = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".",
              "?", "%", "!", "^", "$", "£", ",", "@", "&", "(", ")"]

print("_________________Here are your passwords:____________________\n")

for i in range(passNumber):
    passwords = ''
    for j in range(passLength):
        passwords += random.choice(passChoice)
    print(passwords)
