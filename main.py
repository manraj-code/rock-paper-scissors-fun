import random

# mapping numerical values to String
'''
1 - Stone
0 - Paper
-1 - Scissor
'''

# Randomly choose the computer's choice from the list [1, 0, -1]
computer = random.choice([1, 0, -1])

# Take the user's input (s for Stone, p for Paper, ss for Scissor)
you = input("Enter your choice (s - Stone, p - Paper, ss - Scissor): ")

# Dictionary to map user's input string to the corresponding numerical value
youDect = {"s": 1, "p": 0, "ss": -1}

# Dictionary to map numerical values back to their respective choices for display
reverseDect = {1: "stone", 0: "paper", -1: "scissor"}

# Convert the user's input into the numerical representation
youChoice = youDect[you]

# Display the choices made by the user and the computer
print(f"Your Choice: {reverseDect[youChoice]} \n Computer Choice: {reverseDect[computer]}")

# Check if the user and computer made the same choice
if youChoice == computer:
    print("It's a Draw")
else:
    # Determine the winner based on the game's rules
    if computer == 1 and youChoice == 0:
        print("You Win")  # Paper wraps Stone
    elif computer == 1 and youChoice == -1:
        print("You Lose.!")  # Stone crushes Scissor
    elif computer == 0 and youChoice == 1:
        print("You Lose.!")  # Paper wraps Stone
    elif computer == 0 and youChoice == -1:
        print("You Win")  # Scissor cuts Paper
    elif computer == -1 and youChoice == 1:
        print("You Win")  # Stone crushes Scissor
    elif computer == -1 and youChoice == 0:
        print("You Lose.!")  # Scissor cuts Paper
    else:
        print("Something went wrong")  # This should never be reached
