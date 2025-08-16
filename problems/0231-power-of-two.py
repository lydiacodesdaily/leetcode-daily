# LeetCode 231 - Power of Two
# https://leetcode.com/problems/power-of-two/
#
# ✅ Problem:
# Given an integer n, return True if it is a power of two. Otherwise, return False.
#
# 📚 Pattern:
# Bit Manipulation OR Simple Division Loop
#
# 🔍 Core Idea (Bit Trick):
# A positive power of two has exactly ONE '1' bit in binary.
# Example powers of two:
#   1  = 0001
#   2  = 0010
#   4  = 0100
#   8  = 1000
# Notice: always exactly one '1'.
#
# The trick: (n & (n-1)) clears the lowest set bit in n.
# - If n has only one '1' (i.e., n is a power of two), this becomes 0.
# - Otherwise, result ≠ 0.
#
# Example:
#   n   = 8  (1000)
#   n-1 = 7  (0111)
#   n & (n-1) = 0000 → True
#
#   n   = 12 (1100)
#   n-1 = 11 (1011)
#   n & (n-1) = 1000 ≠ 0 → False
#
# Also require n > 0 (since 0 or negatives aren’t powers of two).
#
# 🧠 Memory Hook:
# - power of 2 = one '1' in binary
# - check: n > 0 and n & (n-1) == 0
#
# ⏱️ Time Complexity: O(1)
# 💾 Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bit trick: check exactly one '1' in binary
        return n > 0 and (n & (n - 1)) == 0


# ---------------------------------------------------------------
# 🔄 Alternative Solution: Repeated Division
#
# Idea:
# Keep dividing n by 2 while it's even. 
# If we end up at 1, then it's a power of two.
#
# Example: n = 16
#   16 % 2 == 0 → n = 8
#   8 % 2 == 0 → n = 4
#   4 % 2 == 0 → n = 2
#   2 % 2 == 0 → n = 1 → return True
#
# Edge case: n == 0 → False
#
# ⏱️ Time Complexity: O(log n)   (divide by 2 until reaching 1)
# 💾 Space Complexity: O(1)

class SolutionDiv:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2    # integer division
        return n == 1


# ---------------------------------------------------------------
# ✅ Complexity Comparison:
# - Bit Trick: O(1) time, O(1) space
# - Division Loop: O(log n) time (because we divide by 2 each step), O(1) space
#
# 👉 Both are fine in interviews.
#    Bit manipulation is the "optimal trick" (faster & elegant).
#    Division is perfectly acceptable if you explain it clearly.
# ---------------------------------------------------------------

# 🔄 Quick Dry Runs:
# n = 1 → True
# n = 2 → True
# n = 3 → False
# n = 16 → True
# n = 0 → False
# n = -2 → False