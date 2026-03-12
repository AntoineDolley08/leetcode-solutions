
# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    l, r = 0, len(matrix) - 1
    while l <= r:
        mid = l + ((r - l) // 2)

        if matrix[mid] == target:
            return mid
        elif matrix[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1