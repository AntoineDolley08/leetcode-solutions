
# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# First solution :
# We use one stack and a variable to keep track of the minimum element. 
# When we push an element, we check if it is smaller than the current minimum and update the minimum accordingly.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min :
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min :
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    
# Time complexity : O(1) for all operations. We push and pop from the stack in constant time and we keep track of the minimum element in constant time.
# Space complexity : O(n) where n is the number of elements in the stack.