class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left: int = 0
        right: int = len(arr) -1
        while left + 1 < right and arr[left] < arr[left + 1]:
            left += 1
        while right - 1 > 0 and arr[right - 1] > arr[right]:
            right -=1
        return left == right 
    
# Separate two-pointer approach
# Increase left index till it does not fulfill the condition
# Decrease right index till it does not fulfill the condition
# Compare left == right?