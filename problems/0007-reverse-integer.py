# LeetCode 7 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/

# ✅ Problem:
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit range [-2^31, 2^31 - 1], return 0.

# 📚 Pattern:
# Math / Digit Extraction

# 🔍 Key Insight:
# Use modulus and integer division to extract and rebuild digits
# Must check for overflow before multiplying

# 🧠 Memory Hook:
# - extract digit: x % 10
# - shift result: res = res * 10 + digit
# - check overflow: res > (MAX - digit) // 10

# ✅ Time Complexity: O(log n) → number of digits in x
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Must check overflow BEFORE updating result
# - Cannot use 64-bit integers
# - Watch for negatives — handle sign separately

class Solution:
    def reverse(self, x: int) -> int:
        # ✅ Define 32-bit int bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        # 🧭 Extract digits one by one
        while x != 0:
            digit = x % 10
            x //= 10

            # 🛑 Overflow check before res * 10
            if res > (INT_MAX - digit) // 10:
                return 0

            # ✅ Build the reversed number
            res = res * 10 + digit

        return sign * res

# 🔄 Dry Run:
# Input: x = 123
# res = 0
# → digit = 3, x = 12 → res = 0 * 10 + 3 = 3
# → digit = 2, x = 1  → res = 3 * 10 + 2 = 32
# → digit = 1, x = 0  → res = 32 * 10 + 1 = 321
# Output = 321 ✅

# Input: x = -120
# → sign = -1
# → digits: 0 → 2 → 1
# → res = 21
# Output = -21 ✅