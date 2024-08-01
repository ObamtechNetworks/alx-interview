#!/usr/bin/python3
"""LockBoxes Programming Challenge"""

from typing import List


def canUnlockAll(boxes: List[list]) -> bool:
    """A function that checks if all lockboxes can be unlocked.

    Args:
        boxes (List[list]): Contains a list of lists of keys to other boxes.

    Returns:
        bool: Returns True if all boxes can be unlocked, False otherwise.
    """
    # Initialize a queue with the key to Box 0
    keys = [0]

    # Use a set to track opened boxes
    opened = set()

    # While there are keys in the queue
    while keys:
        # Get the next key
        key = keys.pop()

        # If the corresponding box hasn't been opened
        if key not in opened:
            # Open the box
            opened.add(key)
            # Add the keys inside this box to our queue of keys
            # Only add keys that are within the range of available boxes
            for new_key in boxes[key]:
                if new_key < len(boxes):
                    keys.append(new_key)

    # Check if we've opened all boxes
    return len(opened) == len(boxes)
