import numpy as np
import random


class Sudoku_grid:
    def __init__(self):
        self.grid = np.zeros((9, 9), dtype=int)

    def print_grid(self):
        print("    1 2 3   4 5 6   7 8 9")
        print("  +-------+-------+-------+")
        for i in range(9):
            print(f"{i+1} |", end=" ")
            for j in range(9):
                print(self.grid[i][j] if self.grid[i][j] != 0 else ".", end=" ")
                if (j + 1) % 3 == 0 and j < 8:
                    print("|", end=" ")
            print("|")
            if (i + 1) % 3 == 0 and i < 8:
                print("  +-------+-------+-------+")
        print("  +-------+-------+-------+")

    def generate(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = 0

    def assign_value(self, row, col, value):
        if self.is_valid_move(row, col, value):
            self.grid[row, col] = value
        else:
            print("Invalid move")

    def is_valid_move(self, row, col, value):
        # Check the row
        for i in range(9):
            if self.grid[row, i] == value:
                return False

        # Check the column
        for i in range(9):
            if self.grid[i, col] == value:
                return False

        # Check the box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i, start_col + j] == value:
                    return False

        return True

    def solve(self, row=0, col=0):
        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0

        if self.grid[row][col] > 0:
            return self.solve(row, col + 1)

        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num

                if self.solve(row, col + 1):
                    return True

            self.grid[row][col] = 0

        return False

    def make_exercise(self, num_empty_cells=20):
        # First, generate a solved Sudoku grid
        self.generate()
        while not self.solve():
            self.generate()

        # Then, remove some numbers from the grid
        for _ in range(num_empty_cells):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row, col] = 0

    def play(self):
        while not self.is_solved():
            self.print_grid()
            row = int(input("Enter the row (1-9): ")) - 1
            col = int(input("Enter the column (1-9): ")) - 1
            value = int(input("Enter the value (1-9): "))
            self.assign_value(row, col, value)

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row, col] == 0 or not self.is_valid_move(
                    row, col, self.grid[row, col]
                ):
                    return False
        return True


# Example of a grid
sudoku = Sudoku_grid()
sudoku.make_exercise()
sudoku.play()
