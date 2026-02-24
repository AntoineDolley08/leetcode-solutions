
# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# First solution : 
# For each string we count the appearance of each letter  and use this as a key in a hashmap to group the anagrams together
from collections import defaultdict
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hash = defaultdict(list)
    for s in strs :
        count = [0] * 26
        for c in s :
            count[ord(c) - ord('a')] += 1
        hash[tuple(count)].append(s)
    return list(hash.values())

# Time complexity : O(n * k) where n is the number of strings in the list and k is the length of the longest string.
# Space complexity : O(n * k) where n is the number of strings and k is the length of the longest string. We store all strings in the hashmap.

# Second solution :
# We can also sort each string and use the sorted string as a key in the hashmap to group the anagrams together.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hash = defaultdict(list)
    for s in strs :
        hash[''.join(sorted(s))].append(s)
    return list(hash.values())

# Time complexity : O(n * k log k) where n is the number of strings in the list and k is the length of the longest string.
# Space complexity : O(n * k) where n is the number of strings and k is the length of the longest string. We store all strings in the hashmap.