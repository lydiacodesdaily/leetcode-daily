# LeetCode 2094 - Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

# ✅ Problem:
# Given an array `digits` (0-9), return all unique 3-digit even numbers 
# that can be formed using the digits at most once.

# 📚 Pattern:
# Brute Force + Frequency Counter

# 🔍 Key Insight:
# - 3-digit even numbers must be in the range [100, 998] and divisible by 2
# - Instead of generating all permutations, iterate all valid numbers directly
# - For each number, check if we have enough of each digit in the original input

# 🧠 Memory Hook:
# - Loop num from 100 to 998 (even)
# - Convert num → digit freq map
# - If freq(num_digits) ≤ freq(input digits) → valid

# ✅ Time: O(1) ≈ 450 iterations
# ✅ Space: O(1) extra + O(output size)

from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_counter = Counter(digits)
        result = []

        for num in range(100, 1000, 2):  # Only 3-digit even numbers
            num_digits = [int(d) for d in str(num)]
            num_counter = Counter(num_digits)

            # Check if all digits needed for `num` are available in input
            if all(num_counter[d] <= digit_counter[d] for d in num_counter):
                result.append(num)

        return result

# 🔄 Dry Run Example:
# digits = [2, 1, 3, 0]
# digit_counter = {2:1, 1:1, 3:1, 0:1}
# Loop num from 100 to 998 (even only):
#   num = 102 → digits = [1,0,2] → valid ✅
#   num = 104 → digits = [1,0,4] → 4 not in input ❌
#   num = 120 → digits = [1,2,0] → valid ✅
#   num = 130 → [1,3,0] → valid ✅
#   ...
# Final result = [102, 120, 130, 132, 210, 230, 302, 310, 312]