"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List
from itertools import product


def combinations_iter(klists):
    for i in product(*klists):
        yield list(i)


def combinations(*klists: List[Any]) -> List[List]:
    result = []
    for i in combinations_iter(klists):
        result.append(i)
    return result
