
# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# First solution
# We use sliding winddow approach, we keep track the character in the current window using a set.

def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    seen = set()
    maxlength = 0
    
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        maxlength = max(maxlength, r - l + 1)
    return maxlength

# Time complexity: O(n) where n is the length of the string. Each character is visited at most twice (once by the right pointer and once by the left pointer).
# Space complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string. In the worst case, we may have to store all.

# Second solution
# We can also use a dictionary to keep track of the last index of each character. When we encounter a repeating character, we can move the left pointer to the right of the last index of that character.

def lengthOfLongestSubstring(self, s: str) -> int:
    char_index = {}
    l = 0
    maxlength = 0
    
    for r in range(len(s)):
        if s[r] in char_index :
            l = max(l, char_index[s[r]] + 1)
        char_index[s[r]] = r
        maxlength = max(maxlength, r - l + 1)
    return maxlength

# Time complexity: O(n) where n is the length of the string. Each character is visited at most once.
# Space complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string. In the worst case, we may have to store all.