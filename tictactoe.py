# tic tac toe

from __future__ import print_function

board = [
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
]

user = True # when user is True it refers to "x"

def print_board(board):
    for row in board:
        for slot in row:
            print(slot + " ", end="")
        print()

def quit(user_input):
    if user_input == "q": return True
    else: return False

def check_input(user_input):
    if 0 < int(user_input) < 10: return True
    else: return False

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)
    if user_input <= 2:
        col = int(user_input)
    else: return (row, col)
    return (row, col)

def add_to_board(coords, board):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user(user)

def active_user(user):
    if user: return "x"
    else: return "o"

def iswin(coords, board):
    for s in board[row].items():
        if s == "x":
            print("Player 1 won!")
            break
        elif s == "o":
            print("Player 2 won!")
            break
        else: continue

while True:
    print_board(board)

    # Player 1
    user_input = raw_input("Player 1, please enter a position 1 through 9 or enter \"q\" to quit. ")
    if quit(user_input): 
        print("Thanks for playing!")
        break

    if not check_input(user_input):
        print("Please enter a number between 1 and 9.")
        continue

    # user input starts from one but indexing starts from 0
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue

    add_to_board(coords, board)

    user = not user # toggle between users