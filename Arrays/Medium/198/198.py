class Solution:
    def rob(self, nums):
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr

# Iterative Dynamic Programming Problem
# 