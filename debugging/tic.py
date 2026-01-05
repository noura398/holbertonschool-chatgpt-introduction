#!/usr/bin/python3

def print_board(board):
    """Print the current Tic-Tac-Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """Return True if there is a winner, otherwise False."""
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    """Return True if no empty spaces remain."""
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board, player):
    """
    Prompt user until they enter a valid (row, col):
    - must be integers
    - must be in range 0..2
    - chosen cell must be empty
    """
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in (0, 1, 2) or col not in (0, 1, 2):
                print("Out of range. Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_valid_move(board, player)
        board[row][col] = player

        # Check win BEFORE switching player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

