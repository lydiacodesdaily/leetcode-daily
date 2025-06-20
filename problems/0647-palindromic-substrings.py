# LeetCode 647 - Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/

# ✅ Problem:
# Given a string `s`, return the number of palindromic substrings in it.
# Each substring must be contiguous and counted individually.

# 🧠 Memory Hook:
# expand around center for all i (odd) and i, i+1 (even)
# count += each time s[left] == s[right]
# O(n^2) centers, O(n^2) expansions

# 📚 Pattern: String Manipulation / Expand Around Center

# ✅ Time Complexity: O(n²) — we try 2n centers and expand each
# ✅ Space Complexity: O(1) — no extra storage besides counters

# 📌 Common Gotchas:
# - Don't forget even-length palindromes (i, i+1)
# - Count every valid expansion (not just longest)

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for i in range(len(s)):
            total += expand(i, i)     # odd-length centers
            total += expand(i, i + 1) # even-length centers

        return total

# 🔁 Example:
# s = "aaa"
# Expand around: (0,0), (0,1), (1,1), (1,2), (2,2)
# Substrings: "a", "aa", "a", "aa", "a" + "aaa"
# Total = 6