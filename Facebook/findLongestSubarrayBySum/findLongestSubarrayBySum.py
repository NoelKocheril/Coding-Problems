#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# You have an unsorted array arr of positive integers and a number s.
# Find a longest contiguous subarray in arr that has a sum equal to s.
# Return two integers that represent its inclusive bounds.
# If there are several possible answers, return the one with the smallest left bound.
# If there are no answers, return [-1].


def findLongestSubarrayBySum(arr: List[int], s: int) -> List[int]:
    """Brute Force Attempt at solving the SumOfTwo problem.

    :param arr: The unsorted array
    :param s: The Target Sum
    :returns: A 1 indexed array of the indexes for the Subarray that sums to the target sum;
    If there is no answer, return [-1]
    """

    pass


def main():
    print(findLongestSubarrayBySum(
        arr=[5, 3, 5, 6, 7],
        s=8)
    )


if __name__ == "__main__":
    main()
