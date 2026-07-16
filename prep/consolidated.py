#1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], i]
            seen[num] = i

#36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if(("row", r, value) in seen or
                    ("col", c, value) in seen or
                    ("box", r//3, c//3, value) in seen):
                    return False
                seen.add(("row", r, value))
                seen.add(("col", c, value))
                seen.add(("box", r//3, c//3, value))
        return True

#49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())

#128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
             

#217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)               
        return False
    
#238. Product of Array Except Self
# No division + division by zeros will break it
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(n):
            answer[i] = left
            left  *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = right * answer[i]
            right *= nums[i]
        return answer

#242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    
#271. Encode and Decode Strings:
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res



#347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+ 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        result = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

#724 - find pivot index
#1991 - find the middle index in array

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
      right = total - left - nums[i]
      if right == left:
        return i
      left += nums[i]
    return -1
    


#567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2) - k + 1):
            window = s2[i: i + k]
            if string1 == Counter(window):
                return True
        return False
    
#567 V2 (Sliding Approach)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        P = Counter(s1)
        k = len(s1)
        if len(s2) < k:
            return False

        window = Counter(s2[:k])
        if window == P:
            return True

        for i in range(k, len(s2)):
            window[s2[i]] += 1
            window[s2[i - k]] -= 1
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]
            if window == P:
                return True
        return False
        
# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = Counter(p)
        k = len(p)
        output = []
        for i in range(len(s) - k + 1):
            window = s[i: i+k]
            if P == Counter(window):
                output.append(i)
        return output

#438 V2 (Sliding Approach)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = Counter(p)
        k = len(p)
        output = []
        if len(s) < k:
            return output
        
        window = Counter(s[:k])
        if window == P:
            output.append(0)
        for i in range(k, len(s)):
            window[s[i]] += 1
            window[s[i-k]] -= 1
            if window[s[i-k]] == 0:
                del window[s[i-k]]
            if window == P:
                output.append(i-k+1)
        return output
    
# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
    
#209. Minimum Size Subarray Sum (Med)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
        
#829. Consecutive Numbers Sum (Hard) 
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        length = 1 
        while length*(length-1)//2 < n:
            remainder = n - length*(length-1)//2
            if remainder % length == 0:
                count += 1
            length += 1
        return count   
    
#1768. Merge Strings Alternately (Easy)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
    
#1710. Maximum Units on a Truck (Easy)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        remaining = truckSize
        output = 0
        for boxes, units in boxTypes:
            take = min(boxes, remaining)
            output += take * units
            remaining -= take
            if remaining == 0:
                break
        return output

        
#416. Partition Equals Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        reachable = {0}
        for n in nums:
            new_sums = set()
            for s in reachable:
                if s + n == target:
                    return True
                if s + n < target:
                    new_sums.add(s + n)
            reachable |= new_sums
        return False

#V2. DP format


#474. Ones and Zeroes (Medium)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            z, o = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i+1, m, n)
            if z <= m and o <= n:
                dp[(i, m, n)] = max(dp[(i, m, n)], 1 + dfs(i+1, m-z, n-o))
            return dp[(i, m, n)]
        return dfs(0, m, n)

#322. Coin Change (Medium)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder < 0:
                return float('inf')
            if remainder in memo:
                return memo[remainder]
            best = float('inf')
            for c in coins:
                best = min(best, 1 + dfs(remainder - c))
            memo[remainder] = best
            return best
        result = dfs(amount)
        return result if result != float('inf') else -1
    
# 2563. Count the Number of Fair Pairs

# 532. K-diff Pairs in an Array (Medium)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_count = Counter(nums)
        output = 0
        for key in nums_count:
            if k == 0 and nums_count[key] >= 2:
                output += 1
            elif k > 0 and key + k in nums_count:
                output += 1
        return output
    

# 1014. Best Sightseeing Pair (Medium)
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_i = values[0] + 0
        answer = 0
        for j in range(1, len(values)):
            answer = max(answer, best_i + values[j] - j)
            best_i = max(best_i, values[j] + j)
        return answer
    
# 350. Intersection of Two Arrays II (Easy)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        C = Counter(nums1)
        output = []
        for num in nums2:
            if C[num] > 0:
                output.append(num)
                C[num] -= 1
        return output
    
# 349. Intersection of Two Arrays II (Easy)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# 657. Robot return to origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for m in moves:
            if m == "U":
                y += 1
            if m == "D":
                y -= 1
            if m == "R":
                x += 1
            elif m == "L":
                x -= 1
        return x == 0 and y == 0
    
# 657 (V2. Robot return to origin (Easy)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        return c["U"] == c["D"] and c["L"] == c["R"]
        
# 874. Walking Robot Simulation (Medium)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]   
        obstacle_set = {tuple(o) for o in obstacles}
        x, y, k = 0, 0, 0                        
        ans = 0
        for c in commands:
            if c == -1:                          
                k = (k + 1) % 4
            elif c == -2:                        
                k = (k - 1) % 4
            else:                                
                dx, dy = dirs[k]
                for _ in range(c):
                    if (x + dx, y + dy) in obstacle_set:
                        break                    
                    x, y = x + dx, y + dy
                    ans = max(ans, x*x + y*y)
        return ans