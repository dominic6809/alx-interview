# 0x07-rotate_2d_matrix
# Rotate 2D Matrix

This project contains a Python function that rotates a given `n x n` 2D matrix by 90 degrees clockwise, in-place.

## Requirements

- **Python Version**: The code is designed to run with Python 3.8.10.
- **Style Guide**: Code should adhere to `pycodestyle` (version 2.8.0).
- **Execution**: All scripts must be executable.
- **No Imports**: The solution should not import any additional modules.
- **Documentation**: All modules and functions must be documented.

## Files

- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix` function implementation.
- `main_0.py`: Script to test the function.

## Function Description

### `rotate_2d_matrix(matrix)`

Rotates a given `n x n` 2D matrix 90 degrees clockwise, in-place.

#### Parameters:
- `matrix` (list of list of int): The `n x n` matrix to be rotated.

#### Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
