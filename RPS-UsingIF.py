#Program to play Rock, Paper and Scissor with the computer
import random

print("Controls:")
print("Scissors = 'S',\n Paper = 'P',\n Rock = 'R',")

user = input("User: ")
computer= random.choice(["R","P","S"])
print("Computer: " + computer)

if user == computer:
    print("\033[1mTie\033[1m")
else:
    if user == "S":
        if computer == "R":
            print("\033[1m Computer wins!! \033[1m")
        else: 
            print("\033[1mUser wins\033[1m")
    elif user == "R":
        if computer == "S":
            print("\033[1mUser wins!!\033[1m")
        else:
            print("\033[1mComputer wins!!\033[1m ")
    else: 
        if computer== "S":
            print("\033[1mComputer wins!!\033[1m")
        else:
            print("\033[1m User wins!! \033[1m")



