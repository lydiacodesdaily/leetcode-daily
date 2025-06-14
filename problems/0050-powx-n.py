# LeetCode 50 - Pow(x, n)
# https://leetcode.com/problems/powx-n/

# ✅ Problem:
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# 🔍 Key Insight:
# Instead of multiplying x by itself n times, break the exponent n into binary bits and repeatedly square the base.
# This is known as **binary exponentiation**.

# 🔁 Key Observations:
# - Any exponent n can be written in binary.
# - For example: x^10 → x^(1010) → x^8 * x^2
# - You only multiply when the current bit is 1.

# ✅ Time Complexity: O(log n) — we divide n by 2 each iteration
# ✅ Space Complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        # Loop until n becomes 0
        while n:
            # If the current bit is 1, multiply result by x
            if n % 2:
                result *= x
            # Square the base for the next bit
            x *= x
            # Move to the next bit (divide n by 2)
            n //= 2

        return result

# 🔄 Dry Run:
# x = 2.0, n = 10
# Binary of 10: 1010
# result = 1
# Step 1: n = 10 → even → x = 4.0, n = 5
# Step 2: n = 5 → odd → result *= 4 → result = 4.0, x = 16.0, n = 2
# Step 3: n = 2 → even → x = 256.0, n = 1
# Step 4: n = 1 → odd → result *= 256 → result = 1024.0, x = 65536.0, n = 0

# 🔁 Final result = 1024.0

# 📌 Common Gotchas:
# - Forgetting to handle negative exponent
# - Mixing up squaring vs multiplying when bit is 1
# - Off-by-one errors in loop termination

# 📚 Pattern: Math / Exponentiation by Squaring
# This approach reduces time complexity from O(n) → O(log n)
