# LeetCode 247 - Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/

# ✅ Problem:
# Given an integer n, return all strobogrammatic numbers that are of length n.

# 🔍 Core Idea:
# Build the number from **outside-in** using backtracking.
# Valid digit pairs: ['0', '0'], ['1', '1'], ['6', '9'], ['9', '6'], ['8', '8']
# Edge case: outermost digit cannot be '0' unless n == 1
# Base cases:
# - When n == 0 → return [""]
# - When n == 1 → return ["0", "1", "8"]

# ✅ Time Complexity: O(5^(n/2)) - 5 choices per pair
# ✅ Space Complexity: O(n) - recursion depth

# 📚 Pattern: Backtracking (build outside-in)

from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 🔗 Helper function for recursive construction
        def build(n, total_length):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            middles = build(n - 2, total_length)
            res = []

            for middle in middles:
                for a, b in [('0', '0'), ('1', '1'), ('6', '9'), ('9', '6'), ('8', '8')]:
                    if n == total_length and a == '0':
                        continue  # Skip leading zeros
                    res.append(a + middle + b)

            return res

        return build(n, n)

# 🔄 Dry Run:
# Input: n = 2
# middles = build(0) → [""]

# Loop:
# '0' + "" + '0' → "00" (skipped because leading 0)
# '1' + "" + '1' → "11"
# '6' + "" + '9' → "69"
# '9' + "" + '6' → "96"
# '8' + "" + '8' → "88"

# Output: ["11", "69", "96", "88"]

# 📌 Common Gotchas:
# - Don't allow leading zeros when n > 1
# - Make sure to return empty string base case for even length

# 🧠 Memory Hook:
# build outside-in → valid pairs → skip leading zero if n > 1 → base case: n == 0 [""] and n == 1 ["0", "1", "8"]