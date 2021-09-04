# Find Longest Sub-array by Sum

## Definition:

You have an unsorted array arr of positive integers and a number s. \
Find a longest contiguous subarray in arr that has a sum equal to s. \
Return two integers that represent its inclusive bounds. \
If there are several possible answers, return the one with the smallest left bound. \
If there are no answers, return [-1].

## Examples

### Example 1

#### Inputs

arr = [1, 2, 3, 7, 5] \
s = 12

#### Output

[2, 4] - The subArray [2, 3, 7] sums up to 12 and since it is 1-based, the starting index is 2 and ending index is 4.

### Example 2

#### Inputs

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] \
s = 15

#### Output

[1, 5] - The subArray [1, 2, 3, 4, 5] sums up to 15 and since it is 1-based, the starting index is 1 and ending index is 5.

### Example 3

#### Inputs

arr = [5, 3, 5, 6, 7] \
s = 4

#### Output

[-1] - None of the subArrays can be equal to the sum of 4, so there is no answer.

## Code Snippet

### Python

```python
#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# You have an unsorted array arr of positive integers and a number s.
# Find a longest contiguous subarray in arr that has a sum equal to s.
# Return two integers that represent its inclusive bounds.
# If there are several possible answers, return the one with the smallest left bound.
# If there are no answers, return [-1].


def findLongestSubarrayBySum(arr: List[int], s: int) -> List[int]:
    """Brute Force Attempt at solving the findLongestSubarrayBySum problem.

    :param arr: The unsorted array
    :param s: The Target Sum
    :returns: A 1 indexed array of the indexes for the Subarray that sums to the target sum;
    If there is no answer, return [-1]
    """

    pass


def main():
    print(findLongestSubarrayBySum(
        arr=[5, 3, 5, 6, 7],
        s=13)
    )


if __name__ == "__main__":
    main()

```
