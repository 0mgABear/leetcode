class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output: List[int] = []
        left = 0
        mid = n
        while left < n:
            output.append(nums[left])
            output.append(nums[mid])
            left += 1
            mid += 1
        return output