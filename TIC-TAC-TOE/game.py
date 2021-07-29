class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # this represents 3x3
        self.current_winner = None

    def print_board(self):
        for row in [self.board[(i*3):(i+1)*3] for i in range(3)]:
            print()
