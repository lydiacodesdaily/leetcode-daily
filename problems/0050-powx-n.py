# LeetCode 50 - Pow(x, n)
# https://leetcode.com/problems/powx-n/

# ✅ Problem:
# Implement pow(x, n) which calculates x raised to the power n (i.e., x^n).
# Constraints:
# - n can be negative
# - You must achieve O(log n) time complexity.

# 🧩 Pattern:
# Fast Exponentiation / Binary Exponentiation

# 🔍 Key Insight:
# You can break exponentiation into halves recursively:
#   - xⁿ = (x²)^(n//2) if n is even
#   - xⁿ = x * (x²)^(n//2) if n is odd
# Use recursion to divide-and-conquer — cutting exponent in half at every step.

# 🧠 Memory Hook:
# - halve exponent each time → log n
# - even → return half * half
# - odd → return half * half * base
# - if n < 0 → flip x and make n positive

# ✅ Time Complexity: O(log n)
# ✅ Space Complexity: O(log n) for recursion (can be O(1) with iteration)

# 📌 Common Gotchas:
# - Negative exponent → x^(-n) = 1 / x^n
# - Be careful with large negative n (e.g., -2^31)
# - Don’t use float power or math.pow
# - Understand the recursive return logic

# Recursive 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 🔄 Handle negative exponent first
        if n < 0:
            x = 1 / x
            n = -n

        # ✅ Recursive fast power
        def fast_pow(base: float, exp: int) -> float:
            # Base case: any number ^ 0 = 1
            if exp == 0:
                return 1.0

            # Recursively compute half power
            half = fast_pow(base, exp // 2)

            # 🔍 This is the core logic:
            # If exponent is even:
            #    xⁿ = (x^(n//2))² → return half * half
            if exp % 2 == 0:
                return half * half
            else:
                # If exponent is odd:
                #    xⁿ = x * (x^(n//2))² → return half * half * base
                return half * half * base

        return fast_pow(x, n)

# 📚 Pattern:
# Binary Exponentiation (Iterative)

# 🔍 Core Idea:
# - Use bitwise operations to exponentiate in O(log n)
# - At each bit: if bit is 1 → multiply result
# - Square x for each shift
# - Handle negative powers with reciprocal

# 🧠 Memory Hook:
# power = abs(n)
# while power:
#   if bit is 1 → multiply result
#   square x
#   shift right
# return 1 / result if n < 0

# ✅ Time Complexity: O(log n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - x^0 = 1.0 even if x == 0
# - x^negative → return 1 / pow(x, -n)
# - Watch integer overflow in other languages

# Iterative 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 🧯 Handle base cases
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = 1
        power = abs(n)
        
        # 🚀 Binary exponentiation
        while power:
            if power & 1:
                result *= x
            x *= x
            power >>= 1
        
        # ↩️ Handle negative exponents
        return result if n >= 0 else 1 / result

# 🔄 Dry Run:
# x = 2.0, n = 10
# binary: 1010
# result *= x^2 * x^8 = 1024

# x = 2.0, n = -2
# power = 2, result = 4, return 1 / 4 = 0.25

# =========================== VERSION 2 =============================
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

"""
Bitwise 
power & 1
This returns:
	•	1 → if the last bit of power is 1 (i.e., power is odd).
	•	0 → if the last bit of power is 0 (i.e., power is even).
"""
