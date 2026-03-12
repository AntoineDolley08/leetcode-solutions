
# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during that hour.
# Return the minimum integer k such that she can eat all the bananas within h hours.


# First solution
# We can use binary search to find the minimum eating speed k to eat all the packs.
# We can set the left pointer to 1 and the right pointer to the maximum number of bananas in a pile.

import math
from typing import List

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(float(pile) / mid)

        if hours > h:
            left = mid + 1
        else:
            right = mid
            res = min(res, mid)

    return res

# Time complexity : O(nlogm) where n is the number of piles and m is the maximum number of bananas in a pile. We are doing binary search on the range of possible eating speeds, which takes O(logm) time. For each eating speed, we are calculating the total hours needed to eat all the bananas, which takes O(n) time.
# Space complexity : O(1) We are not using any extra space.