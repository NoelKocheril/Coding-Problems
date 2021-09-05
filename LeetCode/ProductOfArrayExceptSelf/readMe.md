# Product of Array Except Self

## Definition:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1

#### Inputs

arr = [1, 2, 3, 4]

#### Output

[24, 12, 8, 6]

### Example 2

#### Inputs

arr = [-1, 1, 0, -3, 3]

#### Output

[0, 0, 9, 0, 0]

## Code Snippet

### Python

```python
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

    return []

def main():
    print(ProductOfArrayExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
```
