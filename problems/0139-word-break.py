# LeetCode 139 - Word Break
# https://leetcode.com/problems/word-break/

# ✅ Problem:
# Given a string s and a dictionary of strings wordDict,
# return True if s can be segmented into a space-separated sequence of one or more dictionary words.

# 📚 Pattern:
# Dynamic Programming (1D DP) – Similar to "Unbounded Knapsack"

# 🔍 Key Insight:
# dp[i] = True if s[0:i] can be formed using wordDict
# Can the first i characters broken into to form a valid dict or not?
# For each i from 1 to len(s), try all j < i and check:
#    if dp[j] is True and s[j:i] in wordDict → then dp[i] = True

# 🧠 Memory Hook:
# dp[i] = s[0:i] is breakable
# check all j < i → if dp[j] is True and s[j:i] in wordDict → dp[i] = True

# "Hop + Land" visual:
#   Try hopping from each dp[j] == True to dp[i] if s[j:i] in wordDict
#   You're building up reachable indices based on known words.

# ✅ Time Complexity: O(n^2) — double loop over `s`
# ✅ Space Complexity: O(n) — size of dp array

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert list to set for faster lookups
        word_set = set(wordDict)
        n = len(s)

        # dp[i] = True if s[0:i] is breakable into words
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string is always breakable

        # Build dp[1..n]
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[j:i] is a word AND s[0:j] is breakable
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if dp[i] is True

        return dp[n]  # Whether full string s is breakable



# 🔄 Dry Run:
# s = "leetcode", wordDict = ["leet", "code"]
# dp[4] = True because "leet" is in dict and dp[0] = True
# dp[8] = True because "code" is in dict and dp[4] = True
# Final: dp = [T, F, F, F, T, F, F, F, T] → return dp[8] = True ✅