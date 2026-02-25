
# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# First solution :
# We use a stack to keep track of the opening parentheses.
# We pop from the stack when we encounter a closing parentheses and check if it matches the last opening parentheses.

def isValid(self, s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Time complexity : O(n) where n is the length of the string. We go through the string once to check if the parentheses are valid.
# Space complexity : O(n) We use a stack to keep track of the opening parentheses.
