# LeetCode 5 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# ✅ Problem:
# Given a string `s`, return the longest palindromic substring in `s`.

# 🧠 Pattern: Expand Around Center

# 🔁 Key Observations:
# - A palindrome mirrors around its center.
# - Each character (and gap between characters) can be a center.
# - Expand outward while the characters match.

# 🔍 Visual Example:
# s = "babad"
# Possible centers: "b", "a", "b", "a", "d" and between characters
# "bab" and "aba" are both palindromes

# ✅ Time Complexity: O(n^2) — Expand around each character and each gap
# ✅ Space Complexity: O(1) — No extra space used beyond variables

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around(left, right):
            # Expand while characters match and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # total length of the palindrome

        for i in range(len(s)):
            # Odd length palindrome (centered at i)
            len1 = expand_around(i, i)
            # Even length palindrome (centered between i and i+1)
            len2 = expand_around(i, i + 1)
            max_len = max(len1, len2)

            if max_len > (end - start):
                # 📌 Why (max_len - 1) for start?
                # We round down for start to avoid overshooting left boundary in odd-length cases.
                # For example, max_len = 5 → left shift by 2 from center i
                # 📌 Why no -1 for end?
                # We round up for end to fully capture the right side, esp. in even-length cases.
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

# 🔄 Dry Run:
# Input: "babad"
# Centers considered: i = 0 ('b'), i = 1 ('a'), i = 2 ('b'), ...
# At i = 1 → expands to "aba" or at i = 2 → expands to "bab"
# Longest palindrome = "bab" or "aba"

# 📚 Common Gotchas:
# - Returning substring using `s[start:end+1]`
# - Forgetting to expand for both odd and even centers
# - Off-by-one in bounds or slicing

# 📌 Pattern Summary:
# - For each index in string, expand around it and track max bounds
# - Covers both odd and even palindromes in one loop