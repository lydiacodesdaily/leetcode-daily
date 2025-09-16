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

# LeetCode 139 - Word Break (BFS version)
# https://leetcode.com/problems/word-break/
#
# ✅ Problem:
# Given a string s and a dictionary of strings wordDict, return True if s can be segmented
# into a space-separated sequence of one or more dictionary words.
#
# 📚 Pattern:
# Graph/BFS on index positions (alternative to classic DP)
#
# 🔍 Core Idea:
# Treat each index in s as a node. From index i, you can go to j (i < j ≤ n) if s[i:j] is a word.
# BFS from 0; if we reach n (len(s)), segmentation is possible.
#
# 🧠 Memory Hook:
# indices = nodes
# edge i→j if s[i:j] ∈ dict
# BFS queue of indices
# seen to avoid re-work
#
# ⏱️ Time Complexity:
# Worst-case O(n^2) substring checks (n = len(s)); with a hash set for words.
# (Further optimized by bounding j by max word length if desired.)
# 💾 Space Complexity: O(n) for queue + seen
#
# 📌 Common Gotchas:
# - Forgetting a visited/seen set → exponential blow-up.
# - Scanning all j blindly; consider limiting by max word length for big inputs.
#
# 🧭 Why BFS here vs DP?
# - BFS short-circuits as soon as you can reach the end (good for early exits).
# - Classic DP (dp[i] means s[:i] breakable) is equally valid. Pick one; both are standard.
#
# 🚩 Category Note:
# DP-heavy. Marking: **DP & very unlikely for full-stack E5** (practice once, then deprioritize).
#
# ---------------------------------------------------------------

from typing import List
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BFS over indices
        words = set(wordDict)
        queue = collections.deque([0])  # start at index 0
        seen = set([0])                 # mark 0 as visited

        # Optional micro-optimization: cap window by max word length
        # max_len = max((len(w) for w in words), default=0)

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            # Try all possible end indices
            # for end in range(start + 1, min(len(s), start + max_len) + 1):
            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False

# 🔄 Dry Run:
# s = "leetcode", wordDict = ["leet","code"]
# queue: [0]
# pop 0 -> try "l", "le", "lee", "leet" ✅ enqueue 4; seen={0,4}
# queue: [4]
# pop 4 -> try "c","co","cod","code" ✅ enqueue 8; seen={0,4,8}
# pop 8 == len(s) -> True ✅