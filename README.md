 # **Welcome to Sudoku Delight!** 🧩📝

## **Table of Contents**
1. [**About the Project**](#about)
2. [**Getting Started**](#getting-started)
3. [**Meet Our Sudoku Master: `Sudoku_grid` Class!**](#class)
4. [**How to Play?**](#play)
5. [**Examples and Demonstrations**](#examples)
6. [**Contributing**](#contribute)
7. [**Contact Me**](#contact)
8. [**License**](#license)

## **<a name="about">About</a>**
🧩 **Sudoku Delight!** is a simple Python project designed to create, solve, and play Sudoku puzzles with ease and fun! 🤓

## **<a name="getting-started">Getting Started</a>**
To get started, first make sure you have Python installed on your machine. Then, clone this repository:

```bash
git clone https://github.com/niels-demeyer/sudoku-delight.git
cd sudoku-delight
```

Next, install the required packages by running:

```bash
pip install numpy
```

 ## **<a name="class">Meet Our Sudoku Master: `Sudoku_grid` Class</a>** 🏆

The heart of our project is the `Sudoku_grid` class, which manages creating new puzzles, solving existing ones, and playing the game. Here's an overview of its methods:

### **Methods**

| Method | Description |
| --- | --- |
| `__init__` | Initializes a new instance of the class, creating a 9x9 grid filled with zeros. |
| `print_grid` | Prints the current state of the grid to the console. |
| `generate` | Resets the grid to an empty state (all zeros). |
| `assign_value(row, col, value)` | Assigns a value to a specific cell in the grid, if the move is valid. |
| `is_valid_move(row, col, value)` | Checks if a move (assigning a value to a cell) is valid according to Sudoku rules. |
| `is_valid_sudoku` | Checks if the current state of the grid is a valid Sudoku (i.e., no rules are broken). |
| `is_valid_group(group)` | Checks if a group (row, column, or box) contains all numbers from 1 to 9. |
| `solve(row=0, col=0)` | Solves the Sudoku using a backtracking algorithm. |
| `make_exercise` | Generates a new Sudoku puzzle with a specified difficulty level. |
| `play` | Starts a game, allowing the user to enter values into the grid until the Sudoku is solved. |
| `is_solved` | Checks if the Sudoku has been solved. |

## **<a name="play">How to Play?</a>** 🎲
To play the game, simply call `make_exercise()` and `play()` methods on an instance of `Sudoku_grid`. The game will ask for user input to fill in missing numbers.

```python
sudoku = Sudoku_grid()
sudoku.make_exercise()
sudoku.play()
```

## **<a name="examples">Examples and Demonstrations</a>** 📹
Check out the following examples to see `Sudoku_grid` in action:

1. Creating a new puzzle:

   ```python
   sudoku = Sudoku_grid()
   sudoku.make_exercise()
   sudoku.print_grid()
   ```

2. Solving an existing puzzle:

   ```python
   sudoku = Sudoku_grid()
   sudoku.make_exercise()
   sudoku.solve()
   sudoku.print_grid()
   ```

3. Playing the game:

   ```python
   sudoku = Sudoku_grid()
   sudoku.make_exercise()
   sudoku.play()
   ```

## **<a name="contribute">Contributing</a>** 🤝
I'd love to have you on board! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

## **<a name="contact">Contact Us</a>** 💬
For any questions or suggestions, please reach out to me at [contact.niels.demeyer@gmail.com](mailto:contact.niels.demeyer@gmail.com).

## **<a name="license">License</a>** 📄
This project is licensed under the MIT License - see the `LICENSE` file for details.
