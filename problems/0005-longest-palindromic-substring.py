# LeetCode 5 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# ✅ Problem:
# Given a string `s`, return the longest palindromic substring in `s`.

# 📚 Pattern:
# Two Pointers (Expand Around Center)

# 🔍 Core Idea:
# A palindrome mirrors around its center. For each index `i`, try to expand:
# - around one character (odd-length), and
# - around two characters (even-length)
# Track and update the longest palindrome found.

# 🧠 Memory Hook:
# expand from each center (i or i, i+1)  
# compare lengths → update start & end of result  
# return s[start:end+1]

# ✅ Time Complexity: O(n²) — for each center, expand up to full string
# ✅ Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0  # indices of longest palindrome

        def expand_from_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right-1) - (left+1) + 1  # length of the palindrome
            # after while loop, left & right overshoot by 1
            # valid palindrome = [left+1 : right-1]
            # → len = right - left - 1

        for i in range(len(s)):
            len1 = expand_from_center(i, i)     # odd-length center
            len2 = expand_from_center(i, i + 1) # even-length center
            max_len = max(len1, len2)

            if max_len > (end - start):
                # Update start and end based on max_len and current index i
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

def getLongestPal(s):
    n = len(s)
    start, maxLen = 0, 1
    for i in range(n):
        for j in range(2):  # odd & even centers
            l, r = i, i+j
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1 > maxLen:
                    start, maxLen = l, r-l+1
                l -= 1
                r += 1
    return s[start:start+maxLen]

# 🔄 Dry Run:
# Input: s = "babad"
# Possible centers:
# i = 0 → "b"
# i = 1 → "bab", "aba"
# i = 2 → "a"
# max = "bab" or "aba"
# Output: "bab"