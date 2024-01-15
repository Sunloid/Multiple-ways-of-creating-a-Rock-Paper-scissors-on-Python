#Program to play Rock Paper Scissors with the computer using a tuple
import random

options = ("Rock", "Paper", "Scissor")
Player = None
Computer = random.choice(options)

Player = input("Enter your option: ('Rock', 'Papper', 'Scissor'):")

while Player not in options: 
    print("Please enter a valid input: ('Rock', 'Papper', 'Scissor'):")
    break
else: 
    print(f"Player: {Player}")
    print(f"Computer: {Computer}")
    if Player == Computer:
        print("\033[1m Its a tie!!\033[1m")
    elif (Player == "Rock" and Computer == "Scissor") or (Player == "Scissor" and Computer == "Paper") or (Player == "Paper" and Computer == "Rock"):
        print("\033[1m User won !! \033[1m")
    else:
        print("\033[1mComputer won!!\033[1m")