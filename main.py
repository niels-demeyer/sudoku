import numpy as np


class Sudoku_grid:
    def __init__(self):
        self.grid = np.zeros((9, 9), dtype=int)

    def generate(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = 0

    def print_grid(self):
        print(self.grid)

    def assign_value(self, row, col, value):
        self.grid[row, col] = value

    def make_exercise(self):
        pass


# Example of a grid
sudoku = Sudoku_grid()
sudoku.generate()
sudoku.print_grid()
sudoku.assign_value(0, 0, 5)  # assigns 5 to the cell at the first row and first column
sudoku.print_grid()
