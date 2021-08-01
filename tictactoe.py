# tic tac toe

from __future__ import print_function

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
    if col == 0:
        col = int(user_input)
    else: return (row, col)
    return (row, col)

def add_to_board(coords, board):
    row = coords[0]
    col = coords[1]
    board[row][col] = "x"

while True:
    print_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit. ")
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