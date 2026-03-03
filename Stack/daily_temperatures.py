
# 739. Daily temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Brute force solution 
# For each temp we check in the array when there will be a greater temp.

from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = []
    for i in range(n):
        count = 1
        j = i + 1
        while j < n :
            if temperatures[j] > temperatures[i]: 
                break 
            j+=1
            count+=1
        count = 0 if j==n else count 
        res.append(count)
    return res

# Time complexity : O(n^2) For each element we go through the list, therefore n(n-1)/2 operations donc n^2
# Space complexity : O(n) We alloocate an array of n for the output

# First solution :
# We keep track of the days that have not found a greater temp in a stack and if we find a greater temp we pop the stack for every lower temp.


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, index = stack.pop()
            res[index] = i - index
        stack.append([t, i])

    return res

# Time complexity : O(n) Each element is pushed onto the stack exactly once and poped at most once.
# So in the worst case we have 2n iterations 
# Space complexity : O(n) We allocate for the res and the stack so a most 2n
