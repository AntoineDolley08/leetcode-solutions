
# 125. Valid Palindrome 
# Given a string s, return true if it is a palindrome, or false otherwise.

# First solution :
# Remove all the non alphanumeric characters, create a copy of the string reverse it and then compare

def isPalindrome(self, s: str) -> bool:
    st = [l for l in s.lower() if l.isalnum()]
    s2 = st[::-1]
    return st == s2

# Time complexity : O(n) We build the list in one pass, reverse it and compare
# Space complexity : O(n) We allocate a list of at most n characters

# Second solution : 
# We use two pointers one at the end and one at the start and we check if what they point to is equal and we avoid non alphanumeric

def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1 

    while l < r : 
        if not  s[l].isalnum():
            l+=1
            continue 
        if  not  s[r].isalnum():
            r-=1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

# Time complexity : O(n) Each character is visited at most once as l and r only move towards the center
# Space complexity : O(1) Only two pointer variables, no extra allocation
