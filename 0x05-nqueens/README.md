# 0x05-nqueens
This project provides a solution to the N Queens puzzle, where the task is to place N non-attacking queens on an N×N chessboard.

## Problem Description

- The program solves the N Queens problem using a backtracking algorithm.
- The goal is to place N queens on a chessboard such that no two queens attack each other.
- Each solution is printed as a list of coordinates where each queen is placed on the board.

## Requirements

- **Python 3** must be used.
- The program is designed to take in a single argument, N, which is the size of the chessboard.
- N must be an integer greater than or equal to 4.
- The program prints all possible solutions for placing N queens on the board.

## Usage

Run the program from the command line with the following syntax:

Where:
- `N` is the size of the chessboard (an integer greater than or equal to 4).

### Example:

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
## Input Validation
    If the program is called with incorrect arguments, it will display an error message and exit with status 1.
    If N is not an integer, the program will display "N must be a number".
    If N is less than 4, the program will display "N must be at least 4".

## Code Structure
    is_safe(board, row, col, N): A helper function to check if it's safe to place a queen at a given position.
    solve_nqueens(N): Main function to solve the N Queens problem using backtracking.
    main(): Handles input and validates arguments.
