# LeetCode 392 - Is Subsequence
# https://leetcode.com/problems/is-subsequence/

# ✅ Problem:
# Given two strings `s` and `t`, return true if `s` is a subsequence of `t`.
# A subsequence is a string that can be formed by deleting some (or no) characters of another string,
# without changing the relative order of the remaining characters.

# 📚 Pattern:
# Two Pointers

# 🔍 Key Insight:
# - Use two pointers to walk through both strings.
# - If characters match, move pointer in `s`.
# - Always move pointer in `t`.
# - If `s` is fully consumed, it's a subsequence.

# 🧠 Memory Hook:
# s[i] == t[j] → i++
# always j++
# at end: i == len(s) → True

# ✅ Time Complexity: O(n), where n = len(t)
# ✅ Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# 🔄 Dry Run Example:
# Input: s = "abc", t = "ahbgdc"
# Match: a == a → i=1
# Skip: h ≠ b
# Match: b == b → i=2
# Match: c == c → i=3
# ✅ i == len(s) → return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))  # True
    print(sol.isSubsequence("axc", "ahbgdc"))  # False
    print(sol.isSubsequence("", "ahbgdc"))     # True (empty string is always a subsequence)
    print(sol.isSubsequence("abc", ""))        # False