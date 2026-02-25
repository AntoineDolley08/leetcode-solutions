
# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Naive solution :
# For each elements in the list we calculate the product of all the elements except the current element. 
from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)) :
        product = 1
        for j in range(len(nums)) :
            if i != j :
                product *= nums[j]
        res.append(product)
    return res
# Time complexity : O(n^2) where n is the number of elements in the array. We go through the array twice to calculate the product of all the elements except the current element.
# Space complexity : O(n) We store the result in a new array.

# First solution :
# We iterate over the list to calculate the product of all the elements then we iterate again to to devide the product by the current element.
# If n is 0 we return 0 for all the elements except the one that is 0, for which we return the product of all the elements except 0.
from math import prod

def productExceptSelf(self, nums: List[int]) -> List[int]:

    z_count = nums.count(0)
    if z_count > 1:
        return [0] * len(nums)
    if not z_count:
        grand = prod(nums)
        return [grand // n for n in nums]

    # there is one zero in the nums[]
    result = [0] * len(nums)
    result[nums.index(0)] = prod(n for n in nums if n)

    return result

# Time complexity : O(n) where n is the number of elements in the array. We go through the array twice to calculate the product of all the elements and then to calculate the result.
# Space complexity : O(n) We store the result in a new array.

# Second solution :
# We use prefix and postfix products to calculate the product of all elements except the current one without division.
# First pass (left to right) : we fill res[i] with the product of all elements to the left of i (prefix product).
# Second pass (right to left) : we multiply each res[i] by the product of all elements to the right of i (postfix product).

def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1): # iterate from the last index to 0 (reverse order)
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Time complexity : O(n) where n is the number of elements in the array. We go through the array twice to calculate the prefix and postfix products.
# Space complexity : O(1) extra space. O(n) for the output array.