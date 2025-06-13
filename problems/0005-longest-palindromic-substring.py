# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

"""
🧠 Pattern: Expand Around Center
🎯 Problem: Find the longest palindromic (same forwards and backwards) **substring**.
📌 Use Cases:
- DNA sequence analysis
- String normalization and correction
- Substring search problems

⏰ Time Complexity: O(n²)
📦 Space Complexity: O(1)

Why this works:
- For each character and gap, expand outward while the substring is a palindrome.
- Track the longest bounds seen so far.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return "" 
        
        start, end = 0, 0 

        def expanding(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1 
            return right - left - 1  # Correct length of palindrome

        for i in range(len(s)):
            len1 = expanding(i, i)       # Odd-length center
            len2 = expanding(i, i + 1)   # Even-length center
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2 

        return s[start:end+1]

"""
🧪 Example Test Cases:
s = "babad"
# Output: "bab" or "aba"

s = "cbbd"
# Output: "bb"

s = "a"
# Output: "a"

s = "ac"
# Output: "a" or "c"
"""