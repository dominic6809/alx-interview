# 0x02-minimum_operations

## Description
This project contains a Python method `minOperations(n)` that calculates the fewest number of operations needed to achieve exactly `n` characters in a text file, using only two operations: "Copy All" and "Paste". The problem leverages prime factorization and dynamic programming concepts to minimize the number of operations.

## Prototype
```python
def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in exactly n 'H' characters using 'Copy All' and 'Paste'.
    
    Args:
        n (int): The target number of 'H' characters.
    
    Returns:
        int: The minimum number of operations, or 0 if n is impossible to achieve.
    """
```
## Requirements
    Editor: vi, vim, emacs
    Interpreter: Python 3.4.3 on Ubuntu 20.04 LTS
    PEP 8: Code follows PEP 8 (version 1.7.x) standards.
    Execution: All files must be executable (chmod +x).
    README.md: This file is mandatory and explains the project.
    Documentation: All functions and modules are fully documented.
    Style: Each file ends with a new line.

## Usage
 1. Clone the repository.
 2. Make sure Python 3.4.3 is installed on Ubuntu 20.04 LTS.
 3. Run the main file for testing:
