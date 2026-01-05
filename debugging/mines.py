#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than total cells.")

        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()

        # Header row
        print("  " + " ".join(str(i) for i in range(self.width)))

        for y in range(self.height):
            print(f"{y} ", end="")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print("*", end=" ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else " ", end=" ")
                else:
                    print(".", end=" ")
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                # Don't count the current cell itself
                if dx == 0 and dy == 0:
                    continue

                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Bounds check
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Out of bounds. Try again.")
            return True  # not a loss, just ignore

        # Already revealed
        if self.revealed[y][x]:
            print("That cell is already revealed. Try another one.")
            return True

        # Mine hit
        if (y * self.width + x) in self.mines:
            return False

        # Reveal this cell
        self.revealed[y][x] = True

        # Flood fill if no nearby mines
        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx] and (ny * self.width + nx) not in self.mines:
                            self.reveal(nx, ny)

        return True

    def check_win(self):
        # Win when all non-mine cells are revealed
        for y in range(self.height):
            for x in range(self.width):
                idx = y * self.width + x
                if idx not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
