# tic tac toe

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user = True  # when user is True it refers to "X"


def print_board(board):
    for row in board:
        for slot in row:
            print(slot + " ", end="")
        print()


def quit(user_input):
    if user_input == "q":
        return True
    else:
        return False


def check_input(user_input):
    if 0 < int(user_input) < 10:
        return True
    else:
        return False


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)
    if user_input <= 2:
        col = int(user_input)
    else:
        return (row, col)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diagonal(user, board):
        return True


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != active_user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != active_user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diagonal(user, board):
    complete_diagonal = False
    if (board[0][0] == active_user) and (board[1][1] == active_user) and (board[2][2] == active_user):
        complete_diagonal = True
    if (board[0][2] == active_user) and (board[1][1] == active_user) and (board[2][0] == active_user):
        complete_diagonal = True
    if complete_diagonal:
        return True


while True:
    active_user = current_user(user)
    print_board(board)

    # Player 1
    user_input = input("Player 1, please enter a position 1 through 9 or enter \"q\" to quit. ")
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

    add_to_board(coords, board, active_user)

    if iswin(user, board):
        print_board(board)
        print(f"{active_user.upper()} won!")
        break

    user = not user  # toggle between users
