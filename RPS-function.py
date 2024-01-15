#Program to play Rock Paper Scissors with the computer 
import random

def play():
    print("Controls:")
    print("Scissors = 'S',\n Paper = 'P',\n Rock = 'R',")
    user = input("User: ")
    comp = random.choice(["S","P","R"])
    print("Computer: " + comp)
    
    if user == comp:
        print("\033[1m Tie \033[1m")
    
    elif win(user,comp):
        print("\033[1m User won!! \033[1m")
    
    else:
        print("\033[1m Computer wins!! \033[1m")

def win(player, opponent):
    if (player == "S" and opponent == "P") or (player == "R" and opponent == "S") or (player == "P" and opponent == "R"):
        return True
    
play()

