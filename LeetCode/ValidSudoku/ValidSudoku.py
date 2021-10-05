#!/usr/bin/env python3
from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""


def ValidSudoku(board: List[List[int]]) -> bool:
    """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    * Each row must contain the digits 1-9 without repetition.\n
    * Each column must contain the digits 1-9 without repetition.\n
    * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    :param board: A partially filled 9x9 2D List of ints
    :returns: a boolean value of wheter or not, the board is valid
    """

    # Check Rows
    for i in range(9):
        rowSet = set()
        for j in range(9):
            # print(f"Currently looking at {i},{j}: {board[i][j]}")
            if board[i][j] == ".":
                continue
            elif board[i][j] in rowSet:
                # print(
                #     f"Currently in rowSet: {rowSet}\nLooking at POS x:{i}, y:{j}, Val:{board[i][j]}")
                return False
            else:
                rowSet.add(board[i][j])

    # Check Columns
    for i in range(9):
        colSet = set()
        for j in range(9):
            # print(f"Currently looking at {j},{i}: {board[j][i]}")

            if board[j][i] == ".":
                continue
            elif board[j][i] in colSet:
                # print(
                #     f"Currently in colSet: {colSet}\nLooking at POS x:{i}, y:{j}, Val:{board[j][i]}")
                return False
            else:
                colSet.add(board[j][i])

    # Check 3x3 Grids
    for z in range(3):
        for y in range(3):
            gridSet = set()
            for i in range(3):
                for j in range(3):
                    x_pos = i + (z * 3)
                    y_pos = j + (y * 3)
                    # print(
                    #     f"Currently looking at {x_pos},{y_pos}: {board[x_pos][y_pos]}")
                    if board[x_pos][y_pos] == ".":
                        continue
                    elif board[x_pos][y_pos] in gridSet:
                        # print(
                        #     f"Currently in gridSet: {gridSet}\nLooking at POS x:{i}, y:{j}, Val:{board[x_pos][y_pos]}")
                        return False
                    else:
                        gridSet.add(board[x_pos][y_pos])

    return True


def main():
    # Valid Set
    print(ValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

    # Second Last Row is Invalid
    print(ValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", "4", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

    # 5th Column is Invalid
    print(ValidSudoku(
        [["5", "3", ".", ".", "1", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

    # Middle Section is Invalid
    print(ValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", "3", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))


if __name__ == "__main__":
    main()
