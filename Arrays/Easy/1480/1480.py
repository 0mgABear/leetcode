class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        output = []
        for _ in nums:
            sum += _
            output.append(sum)
        return output