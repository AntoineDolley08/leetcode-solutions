from typing import List

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Naive solution :
# Iterate over the array and for each element n check if the following elements satisfy the condition n + m = target.


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
# Time complexity : O(n^2) We have two nested loops that go through the array.
# Space complexity : O(1) We only use a constant amount of space to store the indices.

# Second solution :
# When iterating over the array we keep track of the element we have seen with hash table with key n and value the index of n.
# For each element we check if the complement target - n is in the hash table. If it is we return the indices of n and target - n.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in hash:
            return [hash[complement], i]
        hash[n] = i
        
# Time complexity : O(n) We go through the array once and the lookup and insertion is O(1) in the hash table.
# Space complexity : O(n) In the worst case with no duplicates we will have to store all the elements in the hash table.

# The second solution is the most optimal one.
