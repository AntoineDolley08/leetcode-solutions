
# 33. Search in Rotated Sorted Array
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# First solution :
# if left part is sorted and target not in rnage of left part search right part 
# else left part not sorted and target not in right part go left 

from typing import List


def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

# Time complexity : O(log(n)) we divide the search space by 2 at each iteration
# Space complexity : O(1) we allocate only 3 variables 