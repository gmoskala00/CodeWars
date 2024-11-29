def who_is_winner(pieces):
    board = {"A": [-1, -1, -1, -1, -1, -1],
             "B": [-1, -1, -1, -1, -1, -1],
             "C": [-1, -1, -1, -1, -1, -1],
             "D": [-1, -1, -1, -1, -1, -1],
             "E": [-1, -1, -1, -1, -1, -1],
             "F": [-1, -1, -1, -1, -1, -1],
             "G": [-1, -1, -1, -1, -1, -1]
        }

    for piece in pieces:
        if "Red" in piece:
            index = len(board[piece[0]]) - 1 - board[piece[0]][::-1].index(-1)
            board[piece[0]][index] = 0
            if is_won(board):
                return "Red"
            continue
        elif "Yellow" in piece:
            index = len(board[piece[0]]) - 1 - board[piece[0]][::-1].index(-1)
            board[piece[0]][index] = 1
            if is_won(board):
                return "Yellow"
            continue
    return "Draw"


def is_won(board):
    board_tab = []
    for _, row in board.items():
        board_tab.append(row)
    for index, row in enumerate(board_tab):
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] != -1:
                return True
    for index, row in enumerate(board_tab[:-3]):
        for i in range(len(row)-3):
            if row[i] == board_tab[index+1][i+1] == board_tab[index+2][i+2] == board_tab[index+3][i+3] != -1:
                return True
        for i in range(3, len(row)):
            if row[i] == board_tab[index+1][i-1] == board_tab[index+2][i-2] == board_tab[index+3][i-3] != -1:
                return True
        for i in range(len(row)):
            if row[i] == board_tab[index+1][i] == board_tab[index+2][i] == board_tab[index+3][i] != -1:
                return True

    return False