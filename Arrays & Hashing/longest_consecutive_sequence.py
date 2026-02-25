
# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Naive solution :
# We sort the array and then we iterate through the sorted array to find the longest consecutive sequence.
from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums :
        return 0
    nums.sort()
    longest = 1
    current = 1
    for i in range(1, len(nums)) :
        if nums[i] == nums[i - 1] + 1 :
            current += 1
        elif nums[i] != nums[i - 1] :
            longest = max(longest, current)
            current = 1
    return max(longest, current)

# Time complexity : O(n log n) where n is the number of elements in the array. We sort the array which takes O(n log n) time and then we iterate through the sorted array which takes O(n) time.
# Space complexity : O(1) We use only a constant amount of space to store the longest and current sequence lengths.

# First solution :
# For each element we check if it is the start of a sequence (i.e. if nums[i] - 1 is not in the set) then we iterate through the sequence to find its length and update the longest sequence length.

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums :
        return 0
    hash = set(nums)
    longest = 1
    for n in nums :
        if n - 1 not in hash :
            current = 1
            while n + current in hash :
                current += 1
            longest = max(longest, current)
    return longest

# Time complexity : O(n) where n is the number of elements in the array. 
# We go through the array once to add the elements to the set and then we go through the array again to find the longest consecutive sequence.
# Space complexity : O(n) We store all the elements in the set.

# Second solution :
# We use a hash map that stores sequence lengths at boundary positions.
# When inserting a number, we check the lengths of adjacent sequences (num - 1 and num + 1) and merge them by updating the boundaries.
# This way, each number is processed once and we avoid repeated scans.

from collections import defaultdict

def longestConsecutive(self, nums: List[int]) -> int:
    mp = defaultdict(int)
    res = 0

    for num in nums:
        if not mp[num]:
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num - 1]] = mp[num]
            mp[num + mp[num + 1]] = mp[num]
            res = max(res, mp[num])
    return res

# Time complexity : O(n) where n is the number of elements in the array. Each number is processed once.
# Space complexity : O(n) We store all the elements in the hash map.