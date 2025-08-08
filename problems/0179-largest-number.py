# LeetCode 179 - Largest Number
# https://leetcode.com/problems/largest-number/

# ✅ Problem:
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
# Return the result as a string.

# 📚 Pattern:
# Custom Sort with Comparator (Greedy)

# 🔍 Key Insight:
# To decide order between two numbers a, b (as strings), compare:
#   a + b  vs  b + a
# Place the one that gives the larger concatenation first.

# 🧠 Memory Hook:
# - sort by "a+b > b+a"
# - join, then handle all-zero case → "0"

# ✅ Time Complexity: O(n log n) for sort; comparisons cost up to O(k) where k = max digits
# ✅ Space Complexity: O(n) for string array

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert to strings for concatenation comparisons
        arr = list(map(str, nums))

        # Custom comparator: if a+b > b+a, put a before b
        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1   # a should come first
            if a + b < b + a:
                return 1    # b should come first
            return 0        # equal in ordering

        arr.sort(key=cmp_to_key(cmp))

        # Edge case: if the largest is "0", the whole number is "0"
        if arr[0] == "0":
            return "0"

        return "".join(arr)

# 🔄 Dry Run (conceptual):
# nums = [3, 30, 34, 5, 9]
# Compare by concatenation:
# "9" before "5" before "34" before "3" before "30"
# → "9534330"

# 📌 Interview Tip:
# If you forget cmp_to_key:
#   arr.sort(key=lambda x: x*10, reverse=True)   # works under LeetCode constraints (<=10 digits)
# Still handle the all-zero case afterward.