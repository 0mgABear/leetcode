class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output: int = 0
        hash: dict[int, int] = {}
        
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        
        for count in hash.values():
            if count > 1:
                output += (count * (count - 1)) // 2
        
        return output
