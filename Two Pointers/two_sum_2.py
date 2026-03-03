
# 167. Two Sum II Input Array Is Sorted 
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# First solution : 
# We go through the list and we sum the two edges if the sum is too large we take the next on the right else too small we take the next on the left  
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r :
        sum = numbers[l] + numbers[r]
        if sum < target :
            l +=1 
            continue
        elif sum > target :
            r-=1
            continue
        else : 
            return  [l+1, r+1]

# Time complexity : O(n) l and r each move at most n times total towards the center, never backwards
# Space complexity : O(1) Only two pointer variables, no extra allocation

# Second solution : 
# We use a dict to keep track of the numbers we have seen and their index
from collections import defaultdict

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    mp = defaultdict(int)

    for i, n in enumerate(numbers):
        temp = target - n 
        if mp[temp]:
            return [mp[temp], i+1]
        mp[n] = i + 1
     
# Time complexity : O(n) Single pass over the array
# Space complexity : O(n) The dict can store at most n entries
