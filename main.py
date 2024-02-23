import numpy as np


class Sudoku_grid:
    def __init__(self):
        self.grid = np.zeros((9, 9), dtype=int)

    def print_grid(self):
        print(self.grid)

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

    def make_exercise(self):
        pass


# Example of a grid
sudoku = Sudoku_grid()
sudoku.generate()
sudoku.print_grid()
sudoku.assign_value(0, 0, 5)  # assigns 5 to the cell at the first row and first column
sudoku.assign_value(0, 3, 5)  # assigns 5 where it not valid
sudoku.print_grid()
