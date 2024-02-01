
from bisect import bisect_left


def find_first_occurrence(arr: list[int], target: int) -> int:
    index = bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    else:
        return -1
