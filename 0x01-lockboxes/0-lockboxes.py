#!/usr/bin/python3
"""
Lockboxes module
This module contains a function to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Params:
        boxes (list): A list of lists where each sublist contains keys
                      to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    visited = set()  # Set to track visited boxes
    to_explore = [0]  # Start exploring from box 0

    while to_explore:
        current_box = to_explore.pop()  # Get the next box to explore
        if current_box not in visited:
            visited.add(current_box)  # Mark the current box as visited
            # Check keys in the current box
            for key in boxes[current_box]:
                if key < len(boxes) and key not in visited:
                    to_explore.append(key)  # Add unvisited boxes to explore

    # Check if all boxes have been visited
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
