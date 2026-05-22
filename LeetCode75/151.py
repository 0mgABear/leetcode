# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    

# s.split() — splits into list of words, automatically trims leading/trailing spaces and handles multiple spaces between words
# [::-1] — reverses the list
# " ".join() — joins back with a single space

# No Built In
def reverseWords(s: str) -> str:
    words = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)  # catch last word

    # reverse words array (two pointer)
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return ' '.join(words)

