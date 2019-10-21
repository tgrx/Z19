from typing import Tuple


def compare_triplets(a: Tuple, b: Tuple) -> Tuple:
    first = sum(i > j for i, j in zip(a, b))
    second = sum(i < j for i, j in zip(a, b))
    return first, second
