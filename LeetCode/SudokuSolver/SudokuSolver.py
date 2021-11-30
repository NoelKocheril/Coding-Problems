#!/usr/bin/env python3
from typing import List, Set, Dict, Tuple, Optional, get_origin

# Definition:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def solveSudoku(self, board: List[List[int]]) -> None:
        """Problem.

        :param arr: An array of N integers
        :returns: An array of N integers, where each index is the product of all other indexes
        """
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    for n in range(1, 10):
                        pass
                else:
                    print(board[x][y])

    def possible(self, x, y, n) -> bool:
        global board
        for i in range(0, 9):
            if(board[x][i] == n):
                return False
            if(board[i][y]) == n):
                return False
        return True


def main():
    board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board))


if __name__ == "__main__":
    main()
