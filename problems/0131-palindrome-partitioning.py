# LeetCode 131 - Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
#
# ✅ Problem:
# Partition a string s into all possible lists of substrings such that every substring is a palindrome.
#
# 📚 Pattern:
# Backtracking (DFS) + palindrome check
#
# 🔍 Core Idea:
# - Build partitions from left to right.
# - At index `start`, try every `end` ≥ start.
#   If s[start:end+1] is a palindrome → choose it, recurse from end+1, then backtrack.
#
# 🧠 Memory Hook:
# - for end in range(start..):
#     if is_pal(start,end): pick s[start:end+1]
# - base: start == n → append path[:]
#
# ⏱️ Time: Exponential in worst case (all palindromes), typical backtracking
# 💾 Space: O(n) recursion depth for path

class Solution:
    def partition(self, s: str):
        n = len(s)
        res = []

        # Two-pointer palindrome check
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # Backtracking: build partitions starting at index `start`
        def dfs(start, path):
            # Base case: used entire string → record a copy
            if start == n:
                res.append(path[:])
                return

            # Try all possible cuts s[start:end+1]
            for end in range(start, n):
                if is_pal(start, end):
                    path.append(s[start:end+1])  # choose
                    dfs(end + 1, path)           # explore
                    path.pop()                   # un-choose (backtrack)

        dfs(0, [])
        return res

# 🔄 Example:
# s = "aab"
# start=0: try "a"(0..0) ✓ → path=["a"]
#   start=1: try "a"(1..1) ✓ → path=["a","a"]
#     start=2: try "b"(2..2) ✓ → path=["a","a","b"] → record
#   backtrack to start=1: try "ab"(1..2) ✗
# backtrack to start=0: try "aa"(0..1) ✓ → path=["aa"]
#   start=2: try "b"(2..2) ✓ → path=["aa","b"] → record
# Output: [["a","a","b"],["aa","b"]]