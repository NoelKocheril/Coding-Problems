#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# You have an unsorted array arr of positive integers and a number s.
# Find a longest contiguous subarray in arr that has a sum equal to s.
# Return two integers that represent its inclusive bounds.
# If there are several possible answers, return the one with the smallest left bound.
# If there are no answers, return [-1].


DEBUG = False


def findLongestSubarrayBySum(arr: List[int], s: int) -> List[int]:
    """Brute Force Attempt at solving the findLongestSubarrayBySum problem.

    :param arr: The unsorted array
    :param s: The Target Sum
    :returns: A 1 indexed array of the indexes for the Subarray that sums to the target sum;
    If there is no answer, return [-1]
    """

    max_length = -1
    start_index = -1
    end_index = -1

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr) + 1):
            curr = arr[i:j]
            if DEBUG:
                print(
                    f"""The Current Array is: {curr},
                    The Current Start Index is {i},
                    The Current End Index is {j},
                    The Current Sum is {sum(curr)}
                    The Length of the sub-array is {len(curr)}\n\n""")

            if (sum(curr) == s):
                if DEBUG:
                    print("Sum of Sub-Array matches Target Sum")
                if len(curr) > max_length:
                    start_index = i + 1
                    end_index = j
                    max_length = len(curr)
            elif (sum(curr) > s):
                break

    if start_index == -1:
        return [-1]
    else:
        return [start_index, end_index]


def main():
    print(findLongestSubarrayBySum(
        arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s=15)
    )


if __name__ == "__main__":
    main()
