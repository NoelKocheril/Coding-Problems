#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


def ProductOfArrayExceptSelf(arr: List[int]) -> bool:
    """Problem.

    :param arr: An array of N integers
    :returns: An array of N integers, where each index is the product of all other indexes
    """

    # Initialize the result array
    n = len(arr)
    res = [1] * n

    # Create the products of the left and right hand side
    l_prod = 1
    r_prod = 1

    # Start from the left and multiple the left hand product with current array position, then increment the left hand product
    for i in range(n):
        res[i] *= l_prod
        l_prod *= arr[i]

    # Start from the right and multiple the right hand product with current array position, then increment the right hand product
    for i in reversed(range(n)):
        res[i] *= r_prod
        r_prod *= arr[i]

    return res


"""
Solution Explanation:
arr     |   a   b   c   d
res     |  bcd acd abd abc
left    |   1   a  ab  abc
right   |  bcd cd   d   1

The result is equal to the right * left
"""


def main():
    print(ProductOfArrayExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
