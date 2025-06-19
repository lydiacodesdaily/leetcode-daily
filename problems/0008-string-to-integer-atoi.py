# LeetCode 8 - String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

# ✅ Problem:
# Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (like C/C++’s `atoi`).
# The function discards leading whitespaces, handles optional '+'/'-' sign, parses digits until non-digit char, 
# and clamps to [-2^31, 2^31 - 1] if overflow.

# 📚 Pattern:
# String Manipulation — Controlled Parsing

# 🧪 Subtype:
# Character-by-character parsing, simulation of finite state logic

# 🧠 Memory Hook:
# strip leading space
# check +/- sign
# parse digits only
# clamp to [-2^31, 2^31-1] at end

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Leading whitespace
# - No digits found → return 0
# - Overflow handling
# - Invalid characters after number → ignore

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check if the string is empty after trimming
        if i == n:
            return 0
        
        # Step 3: Check for sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 4: Convert digits to integer
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 5: Handle overflow/underflow
            if num > (INT_MAX - digit) // 10:
            # num * 10 + digit > INT_MAX  >> num > (INT_MAX - digit) // 10
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num

# 🔄 Dry Run:
# Input: "   -42"
# Step 1: skip spaces → i = 3
# Step 2: '-' → sign = -1, i = 4
# Step 3: parse 4 → num = 4 → parse 2 → num = 42
# Step 4: return -42

# Input: "4193 with words"
# → num = 4193, stops at ' ', return 4193

# Input: "words and 987"
# → no valid start, return 0

# Input: "-91283472332"
# → underflow → return INT_MIN = -2^31 = -2147483648