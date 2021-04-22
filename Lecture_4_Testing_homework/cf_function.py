import math
from typing import List


def get_continued_fraction(fraction: str) -> List:
    numerator = int(fraction.split("/")[0])
    denominator = int(fraction.split("/")[1])
    cf = []

    def iteration(num: int, denom: int) -> List:
        first = math.floor(num / denom)
        cf.append(first)
        if num % denom != 0:
            num -= first * denom
            return iteration(denom, num)

    iteration(numerator, denominator)
    return cf