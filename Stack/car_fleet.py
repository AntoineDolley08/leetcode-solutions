
# 853. Car Fleet
# There are n cars going to the same destination along a one lane road. The destination is target miles away.
# You are given two integer array position and speed, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).
# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
# Return the number of car fleets that will arrive at the destination.

# First solution
# We sort the cars in terms of distance to the target. And for each car we compute the time it takes to reach the target. 
# We keep the cars times in a stack and if a car time is less than a car that started before it is addded to the car fleet of the car that started before it.

from ast import List

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

# Time complexity : O(nlogn) We sort the cars by their position, which takes O(nlogn) time. Then we iterate through the sorted list of cars O(n).
# Space complexity : O(n) We allocate a stack that in the worst case can contain all the cars.