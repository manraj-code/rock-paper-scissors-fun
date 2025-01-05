import random

# Assign numerical values for each choice for easier comparison:
'''
1 - Stone
0 - Paper
-1 - Scissor
'''

# Randomly choose the computer's choice
computer = random.choice([1, 0, -1])

# Prompt the user to input their choice: "s" for Stone, "p" for Paper, "ss" for Scissor
you = input("Enter your choice (s - Stone, p - Paper, ss - Scissor): ")

# Dictionary to map the user's input to its respective numerical value
youDect = {"s": 1, "p": 0, "ss": -1}

# Dictionary to convert numerical values back to their respective choices for display
reverseDect = {1: "stone", 0: "paper", -1: "scissor"}

# Convert the user's input into a numerical value
youChoice = youDect[you]

# Display the user's choice and the computer's choice
print(f"Your Choice: {reverseDect[youChoice]} \nComputer Choice: {reverseDect[computer]}")

# Check if the user and computer made the same choice
if youChoice == computer:
    print("It's a Draw")
else:
    # Use the difference (computer - youChoice) to determine the result:
    # -1 or 2 indicates a loss for the user
    # 1 or -2 indicates a win for the user
    if (computer - youChoice) == -1 or (computer - youChoice) == 2:
        print("You Lose..!!")  # Computer wins
    elif (computer - youChoice) == 1 or (computer - youChoice) == -2:
        print("You WIN")  # User wins
    else: 
        print("Something Went Wrong..!!")  # Catch any unexpected logic issues
