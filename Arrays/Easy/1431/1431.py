class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies : int = max(candies)
        output : list = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output