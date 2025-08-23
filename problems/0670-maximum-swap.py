# LeetCode 670 - Maximum Swap
# https://leetcode.com/problems/maximum-swap/
#
# ✅ Problem:
# Given a non-negative integer `num`, you may swap two digits at most once.
# Return the maximum possible value of `num` after one swap (or no swap).
#
# 📚 Pattern: Greedy + Last-Occurrence Index (digits 0..9)
#
# 🔍 Core Idea:
# For each position i (left→right), ask:
#   “Is there a larger digit (9..current+1) that appears somewhere to the RIGHT of i?”
# If yes, swap current digit with the RIGHTMOST occurrence of that larger digit (to maximize the number),
# then return immediately (only one swap allowed).
#
# 🧠 Memory Hook (recall fast):
# - map last index of each digit 0..9
# - scan left→right:
#   for d in 9..curr+1:
#     if last[d] > i → swap with that RIGHTMOST d and return
# - if no swap found → return original
#
# ✅ Time Complexity: O(n + 10n) ≈ O(n)
# ✅ Space Complexity: O(1)   (fixed 10-size array for digits)
#
# ⚠️ Common Gotchas:
# - Must use the *rightmost* occurrence of the larger digit to maximize value.
# - Stop after the first successful swap (most significant change first gives max).
# - Handle numbers with repeated digits correctly (e.g., 1993 → swap 1 with rightmost 9).
#
# 🏷️ Interview Fit:
# - Not DP. Classic greedy with a neat digit-index trick. Very suitable for live interviews.

from typing import List

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert to list of chars for easy swapping
        digits = list(str(num))
        n = len(digits)

        # Step 1) Record the last index where each digit (0..9) appears
        last_index = [-1] * 10
        for i, ch in enumerate(digits):
            last_index[int(ch)] = i

        # Step 2) Scan from left to right and try to upgrade each position
        for i in range(n):
            current = int(digits[i])

            # Try to find a larger digit to swap with, checking from 9 down to current+1
            for candidate in range(9, current, -1):
                j = last_index[candidate]
                # If candidate exists to the RIGHT, swapping increases the number
                if j > i:
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))  # only one swap allowed

        # Step 3) No beneficial swap found → return original
        return num


# 🔄 Dry Run:
# num = 2736
# digits = ['2','7','3','6']
# last_index = [.., 2:'0', 3:'2', 6:'3', 7:'1', ...]  (actual: last positions)
# i=0 ('2'): check 9..3 → first found larger is '7' at j=1 or '6' at j=3 or '3' at j=2
#   we check from 9→3; the first existing is '7' at j=1 (>0) → swap i=0 with j=1 → 7236 → return
#
# num = 9973
# digits = ['9','9','7','3']
# i=0 ('9'): no larger exists
# i=1 ('9'): no larger exists
# i=2 ('7'): check 9..8 → last_index[9]=1, but j=1 is NOT > 2 → cannot swap (left side)
# i=3 ('3'): no larger to the right
# → no swap → return 9973
#
# Embedded Example:
# num = 1993
# digits = ['1','9','9','3']; last_index[9] = 2
# i=0 ('1'): check 9..2 → find 9 at j=2 (>0) → swap → 9913 → return 9913