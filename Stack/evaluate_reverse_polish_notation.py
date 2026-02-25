
# 150. Evaluate Reverse Polish Notation
# Given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation, evaluate the expression.

# First solution :
# We use a stack to evaluate the expression. We add numbers to the stack and when we encounter an operator, we pop the top two elements from the stack, 
# perform the operation and push the result back to the stack.
from typing import List

def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for token in tokens :
        if token in ['+', '-', '*', '/'] :
            b = stack.pop()
            a = stack.pop()
            if token == '+' :
                stack.append(a + b)
            elif token == '-' :
                stack.append(a - b)
            elif token == '*' :
                stack.append(a * b)
            else :
                stack.append(int(a / b))
        else :
            stack.append(int(token))
    return stack[0]

# Time complexity : O(n) where n is the number of tokens in the input array. We iterate through the tokens once and perform constant time operations for each token.
# Space complexity : O(n) in the worst case when all tokens are numbers and we push them to the stack.