def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner on the Tic Tac Toe board.

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    """
    Checks if the game is a draw (all spots are filled and there is no winner).

    Args:
        board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
        bool: True if it's a draw, False otherwise.
    """
    for row in board:
        if " " in row:  # If there is an empty spot, it's not a draw yet
            return False
    return True


def tic_tac_toe():
    """
    Main function to play Tic Tac Toe.

    Alternates between players "X" and "O", asking for input until a winner is found or a draw occurs.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty 3x3 board
    player = "X"  # Player "X" starts the game

    while not check_winner(board):  # Continue playing until there is a winner
        print_board(board)  # Display the current state of the board
        
        while True:
            try:
                # Request row and column inputs from the user
                row_input = input(f"Enter row (0, 1, or 2) for player {player}: ").strip()
                col_input = input(f"Enter column (0, 1, or 2) for player {player}: ").strip()

                # Check for empty inputs
                if not row_input or not col_input:
                    print("Input cannot be empty. Please enter a valid number.")
                    continue

                # Convert the inputs to integers
                row = int(row_input)
                col = int(col_input)

                # Ensure the row and column are within the valid range (0-2)
                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates! Please enter row and column between 0 and 2.")
                    continue

                # Check if the selected spot is already taken
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                # If everything is valid, make the move
                board[row][col] = player
                break  # Exit the loop to switch to the other player

            except ValueError:
                print("Invalid input! Please enter valid integers only.")

        # Switch player after each valid move
        player = "O" if player == "X" else "X"

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

    print_board(board)
    print(f"Player {player} wins!")


if __name__ == "__main__":
    tic_tac_toe()
