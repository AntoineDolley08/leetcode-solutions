
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# First solution : 
# We go throug the array and keep track of the min and the max with 2 pointers and calculate max price at every instance

from typing import List


def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP

# Time complexity : O(n) We go through the array once 
# Space complexity : O(1) we allocate only 3 variables

# Second solution :
# Each day we imagine selling on that day and compare with previous profit we also keep track of lowest selling day

def maxProfit(self, prices: List[int]) -> int:
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)
    return maxP

# Time complexity : O(n) We go through the array once 
# Space complexity : O(1) we allocate only 3 variables
