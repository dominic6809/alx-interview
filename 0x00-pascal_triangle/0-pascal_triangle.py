def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows for Pascal's Triangle. Must be a positive integer.

    Returns:
        list: A list of lists, where each inner list represents a row in Pascal's Triangle.
              If n <= 0, returns an empty list.
    """
    
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Initialize a row with 1s, of length i+1
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)
    
    return triangle
