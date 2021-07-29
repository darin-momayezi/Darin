# tic tac toe

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(slot + " ", end="")
        print()

print_board(board)

def quit(user_input):
    if user_input == "q": return True
    else: return False

def check_input(user_input):
    # check if it is a number
    isnum(user_input)

    # check if it is 1 through 9

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number.")
        return False
    else: return True

while True:
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit. ")
    if quit(user_input): 
        print("Thanks for playing!")
        break

    if not check_input(user_input):
        print("Please enter an number between 1 and 9.")
        continue