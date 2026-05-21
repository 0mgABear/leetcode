# 1071. Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"

# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"

# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"

# Output: ""

# Example 4:

# Input: str1 = "AAAAAB", str2 = "AAA"

# Output: ""​​​​​​​

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


# Core idea: If a GCD string exists, concatenating in both orders must be equal:

# str1 + str2 === str2 + str1
# If not, return ""
# Why? If both strings are made of the same repeating pattern, swapping concatenation order won't change the result.

# Then: The GCD string's length must divide both string lengths evenly — so use gcd(len(str1), len(str2)) to find it, and slice the first that many characters.

# Example:

# str1 = "ABABAB" (len 6)
# str2 = "ABAB"   (len 4)
# gcd(6, 4) = 2
# answer = str1[:2] = "AB"

class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:gcd(len(str1), len(str2))]
        