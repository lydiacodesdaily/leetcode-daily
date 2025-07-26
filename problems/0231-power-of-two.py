# LeetCode 231 - Power of Two  
# https://leetcode.com/problems/power-of-two/

# ✅ Problem:
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# 📚 Pattern:
# Bit Manipulation

# 🔍 Key Insight:
# A power of two has **only one '1' bit** in binary.
#      n     =  00010000
#  n - 1     =  00001111
#  n & (n-1) =  00000000
# So: if (n > 0) and (n & (n - 1)) == 0 → ✅ power of two

# 🧠 Memory Hook:
# - power of two → only one 1 bit
# - formula: n > 0 and (n & (n - 1)) == 0

# ✅ Time Complexity: O(1)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting to check `n > 0`
# - Using floating point math (`log`) — avoid due to precision issues
# - Confusing `(n & (n - 1)) == 1` (wrong!) vs `== 0` (correct)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # ✅ Clean one-liner using bit trick
        return n > 0 and (n & (n - 1)) == 0

# 🔄 Dry Run:
# Input: n = 16
# Binary: 10000
# n-1 = 15 → 01111
# n & (n-1) = 00000 → ✅ return True

# Input: n = 18
# Binary: 10010
# n-1 = 17 → 10001
# n & (n-1) = 10000 → ≠ 0 → ❌ return False