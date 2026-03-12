
# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

from typing import List


def findMin(self, nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]: # The subarray is sroted we take first element
            res = min(res, nums[l])
            break

        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1  # the left part is sorted so the min is in other half
        else:
            r = m - 1 # the min is between left and middle and may be middle
    return res

# Time complexity : O(log(n)) we cut in half the search space every time
# Space complexity : O(1) we only allocate 3 variables