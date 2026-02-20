from collections import defaultdict
from turtle import st
from typing import Counter


# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# First intuition :
# Create a hash map for each string and check if they are equal.

def isAnagram(self, s: str, t: str) -> bool:
    d1 = to_dict(s)
    d2 = to_dict(t)
    return d1 == d2

    
def to_dict(st: str):
    re = defaultdict(int)
    for l in st:
        re[l] += 1
    return re

# Time complexity : O(n + m) We go thourgh both string once and the lookup and insertion is O(1) in the hash table. Then we compare the two hash tables in O(n) time.
# Space complexity : O(n + m) Two dictionaries are created with at most n and m elements.


# Second solution :
# Eliminate cases where the length of the strings are different and then check if the counter of the two strings are equal.

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s)==Counter(t)

# Time complexity : O(n + m) Counter goes through each string once and we compare the two in O(n) time. The length check is O(1).
# Space complexity : O(n + m) Two dictionaries are created with at most n and m elements.


# Third solution :
# We go through both strings at he same time and keep track of the apearence of each character in a hash table. 
# We increment the count for the characters in s and decrement for the characters in t. At the end we check if all the counts are 0.

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in count)

# Time complexity : O(n) We go through both string once and the other operations are O(1).
# Space complexity : O(1) We only use a fixed size array of 26 elements to keep track of the count of each character.

# Fourth solution :
# pour chaque caractère de s on regarde si il y en a le même nombre dans t.

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for c in set(s):
        if s.count(c) != t.count(c):
            return False
    return True

# Time complexity : O(k*n) where k is the number of unique characters in s. We go through each unique character and count its apearence in both string which takes O(n) time.
# In the worst case where all characters are unique we have k = n and the time complexity is O(n^2).

# Space complexity : O(n) We create a set of the characters in s which can have at most n elements.