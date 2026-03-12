
# 74. Search a 2D Matrix
# Given an m x n matrix, where each of the rows is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row, and an integer target, return true if target is in matrix or false otherwise.

# First solution
# We can use binary search to find the target in the matrix. We can treat the matrix as a sorted array and use binary search to find the target.

from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    left, right = 0, ROWS * COLS - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = mid // COLS, mid % COLS
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Time complexity : O(log(m*n)) We are doing binary search on a matrix of size m*n.
# Space complexity : O(1) We are not using any extra space.
