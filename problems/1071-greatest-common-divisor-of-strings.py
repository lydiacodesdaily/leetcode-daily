# LeetCode 1071 - Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# ✅ Problem:
# Given two strings str1 and str2, return the largest string X such that:
# - X divides both str1 and str2 (i.e., str1 = X * n, str2 = X * m for some n, m)
# - If no such string exists, return ""

# 📚 Pattern:
# String GCD pattern + math.gcd on lengths

# 🔍 Key Insight:
# - If str1 + str2 == str2 + str1, then both are made of a common base string
# - Length of the base string = gcd(len(str1), len(str2))

# 🧠 Memory Hook:
# "Check string symmetry → then use math.gcd on lengths"
# - str1 + str2 == str2 + str1
# - Return str1[:gcd(len1, len2)]

# ✅ Time Complexity: O(N + M)
# ✅ Space Complexity: O(1)

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenated strings are not equal, no common base
        if str1 + str2 != str2 + str1:
            return ""

        # Length of common base = gcd of string lengths
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]

# 🔄 Dry Run Example (commented for reference):
# str1 = "ABCABC", str2 = "ABC"
# str1 + str2 = "ABCABCABC"
# str2 + str1 = "ABCABCABC" ✅
# gcd(len(str1), len(str2)) = gcd(6, 3) = 3
# → str1[:3] = "ABC" ✅
