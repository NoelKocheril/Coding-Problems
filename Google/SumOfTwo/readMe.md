# Sum of Two

## Definition:

You have two integer arrays, a and b, and an integer target value v.
Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v.
Return true if such a pair exists, otherwise return false.

## Examples

### Example 1

#### Inputs

First Array = [0, 0, -5, 30212] \
Second Array = [-10, 40, -3, 9] \
Target Value = -8

#### Output

True - The value "-5" in the first array and the value "-3" in the second array can be summed together to hit the target value "-8"

### Example 2

#### Inputs

First Array = [1, 2, 3] \
Second Array = [-10, 40, -3, 9] \
Target Value = 50

#### Output

False - None of the pairs can be summed together to create the target value "50"

## Code Snippet

### Python

```python
#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional

# Definition:
# You have two integer arrays, a and b, and an integer target value v.
# Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
# that can be added together to get a sum of v.
# Return true if such a pair exists, otherwise return false.

def SumOfTwo(a: List[int], b: List[int], v: int) -> bool:
    """Brute Force Attempt at solving the SumOfTwo problem.

    :param a: The First Integer Array
    :param b: The Second Integer Array
    :param v: Target Value
    :returns: A Boolean value of whether or not the two integer arrays can hit the target value
    """

    pass

def main():
    print(SumOfTwo([0, 0, -5, 30212], [-10, 40, -3, 9], -8))


if __name__ == "__main__":
    main()
```
