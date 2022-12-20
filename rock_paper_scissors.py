import random

print("Welcome to rock, paper and scissor game!")

# variable for repeating the game while user wants to play
repeat = "y"

# with this while loop the game will restart
while repeat == "y":
    
    # getting a computers move as a random number which will be compared
    # to index of element of list all_moves
    comp_move = random.choice(["r", "p", "s"])
    print(comp_move)
    # reseting the user_move
    user_move = ""
    
    # getting users move
    while user_move != "r" and user_move != "p" and user_move != "s":
        user_move = input("Pick your move (r, p or s):")
        if user_move != "r" and user_move != "p" and user_move != "s":
            print("Enter a valid input please.")

    # if user and computer make the same move it is a tie
    if comp_move == user_move:
        print ("It's a tie!")
    
    else:
        if (comp_move == "r" and user_move == "p") or (comp_move == "s" and user_move == "r") or (comp_move == "p" and user_move == "s"):
           print("You win!")
        else:
            print("You lost:(") 
    
    # this part of codes asks user if he wants to continue or terminate the game
    repeat = ""
    while repeat != "y" and repeat != "n":    
        repeat = input("Do you want to continue game (y/n)?")
        if repeat != "y" and repeat != "n":
           print("Enter a valid input please.")
         