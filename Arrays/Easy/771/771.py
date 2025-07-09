class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash : dict[str, int] = {}
        output : int = 0
        for char in jewels:
            hash[char] = 1
        for _ in stones:
            if _ in hash:
                output += 1
        return output
    
# create a hash map using jewels
# check stones
# return output as a number


        