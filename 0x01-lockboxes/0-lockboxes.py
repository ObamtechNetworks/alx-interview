#!/usr/bin/python3
"""LockBoxes Programming Challenge"""

from typing import List


def canUnlockAll(boxes: List[list]) -> bool:
    """A function that checks lockboxes
    if all the boxes can be unlocked

    Args:
        boxes (List[list]): Contains a list of lists of keys to other boxes

    Returns:
        bool: returns True if all boxes can be unlocked, false if not
    """
    # IMPLEMENTATION STEPS
    # Initialize a queue with the key to the box
    keys = [0]

    # use a set to track opened boxes: opened = set()
    opened = set()

    # with respect to the given boxes, loop through the keys
    # in the queue until it's empty
    while keys:
        # get the next key
        key = keys.pop()

        # if the corresponding box hasn't been opened
        # oopen it and collect the keys inside
        if key not in opened:
            # open the box
            opened.add(key)

            # add the keys inside this box to our queue of keys
            # only add keys that are within the range of the avaialbe boxes
            for new_key in boxes[key]:
                if new_key < len(boxes):
                    keys.append(new_key)

    # check if we've opened all boxes
    return len(opened) == len(boxes)
