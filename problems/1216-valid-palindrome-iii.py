# LeetCode 1216 - Valid Palindrome III
# https://leetcode.com/problems/valid-palindrome-iii/

# ✅ Problem:
# Given a string s and an integer k, return true if s is a k-palindrome.
# A k-palindrome means: we can delete at most k characters from s to make it a palindrome.

# 📚 Pattern:
# Dynamic Programming (Bottom-Up)
# - Think of this as Longest Palindromic Subsequence (LPS)
# - If len(s) - LPS <= k → then it's a valid k-palindrome

# 🧪 Subtype:
# DP on substring ranges (2D dp[i][j])

# 🧠 Memory Hook:
# LPS = max palin in s[i..j]
# build dp bottom-up by length
# final check: len(s) - dp[0][n-1] <= k

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(n^2)

# 📌 Common Gotchas:
# - The LPS may *not* be contiguous — we're allowing skips
# - You must compare len(s) - LPS vs k (not LPS directly)

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        # 🧱 Step 1: Initialize DP grid
        # dp[i][j] = LPS (Longest Palindromic Subsequence) length in s[i..j]
        dp = [[0] * n for _ in range(n)] # dp[i][j] = min deletions to make s[i..j] a palindrome

        # 🧱 Step 2: Base case — each character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1 # If i == j, it’s a 1-letter substring → it’s already a palindrome

        # 🧱 Step 3: Build bottom-up for substrings of length 2 to n
        for length in range(2, n + 1):            # length of the substring
            for i in range(n - length + 1):       # start index of substring
                j = i + length - 1                # end index of substring

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # 🧮 Step 4: Compare deletions needed vs k
        lps_len = dp[0][n - 1]
        return (n - lps_len) <= k

# 🔄 Dry Run:
# Input: s = "abcdeca", k = 2
# LPS = "acdca" → length = 5
# len(s) = 7 → deletions needed = 2 → return True ✅

# Another example:
# s = "abbababa", k = 1
# LPS = 7 → deletions = 1 → valid