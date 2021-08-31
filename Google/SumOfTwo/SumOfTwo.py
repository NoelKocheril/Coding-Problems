#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# You have two integer arrays, a and b, and an integer target value v.
# Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
# that can be added together to get a sum of v.
# Return true if such a pair exists, otherwise return false.


# def SumOfTwo(a: List[int], b: List[int], v: int) -> bool:
#     """Brute Force Attempt at solving the SumOfTwo problem.

#     :param a: The First Integer Array
#     :param b: The Second Integer Array
#     :param v: Target Value
#     :returns: A Boolean value of whether or not the two integer arrays can hit the target value
#     """

#     # Loop through all entries in a and b, and see if the sum is the target value
#     for int_a in a:
#         for int_b in b:
#             if int_a+int_b == v:
#                 return True

#     # If none of the sums is equal to the target value, return False
#     return False


def SumOfTwo(a: List[int], b: List[int], v: int) -> bool:
    """Optimized Attempt at solving the SumOfTwo problem.

    :param a: The First Integer Array
    :param b: The Second Integer Array
    :param v: Target Value
    :returns: A Boolean value of whether or not the two integer arrays can hit the target value
    """

    # Initialize a set of to hold the compliments of all entries from a against the target value
    # i.e. tv = 7, a = [1, 2, 3] => compliments = (6, 5, 4)
    compliments: Set[int] = set()

    for i in a:
        compliments.add(v - i)

    # Loop through entries in b, if it exists in compliments return True
    for i in b:
        if i in compliments:
            return True

    # If none found, return False
    return False


def main():
    print(SumOfTwo([0, 0, -5, 30212], [-10, 40, -3, 9], -8))


if __name__ == "__main__":
    main()
