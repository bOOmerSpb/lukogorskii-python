from typing import List


def get_continued_fraction(fraction: str) -> List:
    numerator, denominator = map(int, fraction.split("/"))
    cf = []

    def recursion(num: int, denom: int) -> List:
        try:
            first = num // denom
        except ZeroDivisionError:
            return cf

        cf.append(first)
        if num % denom != 0:
            num -= first * denom
            return recursion(denom, num)

    recursion(numerator, denominator)
    return cf
