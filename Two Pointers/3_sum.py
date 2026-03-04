
# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# First solution :
# We sort the array and then we use the algorithm of two sum for each n of the array

from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []

    for i in range(len(nums)) :
        if nums[i] > 0:
            break # if smallest is positive no solutions further

        if i > 0 and nums[i] == nums[i - 1]:
            continue # skip same numbers to avoid duplicate solutions

        l, r = i+1, len(nums) - 1
        while l < r :
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0 :
                l +=1 
                continue
            elif sum > 0 :
                r-=1
                continue
            else : 
                res.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l] == nums[l - 1] :
                    l += 1 # also avoid duplicate solutions

    return res

# Time complexity : O(n^2) - sort is O(n log n) + for loop O(n) * two pointers O(n) = O(n^2)
# Space complexity : O(1) - only pointers and variables, no extra data structure