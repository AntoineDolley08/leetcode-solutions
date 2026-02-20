
from collections import defaultdict
from typing import List

# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# First intuition :
# Iterate over the array and check if the element n has already been seen before.

def containsDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(bool)
        for n in nums :
            if hash[n] :
                return True
            hash[n] = True
        return False

# Time complexity : O(n) We go through the array once and the lookup and insertion is O(1) in the hash table.
# Space complexity : O(n) In the worst case with no dduplicates we will have to store all the elements in the hash table.

# Second solution :
# Check if the Length of the set of the array is different form the length of the array.

def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

# Time complexity : O(n) The set is created in O(n) time and other operations are O(1).
# Space complexity : O(n) The created set contains n elements.

# The two solution have the same complexity. But the first one can be faster if a duplicate 
# is found early within the aray.
# The second solution will allways go through the entire array to create the set.