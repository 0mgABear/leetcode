# 735. Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:

# Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

# Key insight: Collision only happens when stack top is positive (→) and incoming is negative (←). They're moving toward each other.

# Collision only happens when stack top is positive (→) and incoming is negative (←)
# Four cases:
# 1. positive → vs negative ← : COLLISION (moving toward each other)
# 2. positive → vs positive → : no collision (same direction)
# 3. negative ← vs negative ← : no collision (same direction)
# 4. negative ← vs positive → : no collision (moving apart)

# Three outcomes when collision occurs:
# 1. stack top smaller  → stack top explodes, continue (chain collision possible)
# 2. equal size         → both explode, break
# 3. stack top larger   → incoming explodes, break

# Python while/else trick:
# - else block runs only if while exits naturally (condition false)
# - else is skipped if break fires
# - used here to push asteroid only if it survived all collisions

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
        