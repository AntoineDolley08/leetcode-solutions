
# 704. Binary Search 
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# First solution
# Since the input array is sorted we can look in the middle of the array and see if our target is greater or lower to determine the part of the array we search next

from typing import List


def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + ((r - l) // 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Time complexity : O(log(n)) - we divide the search space by 2 at each iteration
# Space complexity : O(1) - only a constant number of variables (l, r, mid)