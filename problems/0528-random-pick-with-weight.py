# LeetCode 528 - Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

# ✅ Problem:
# Given an array of positive integers `w`, where `w[i]` is the weight of index i,
# implement a class `Solution` with the following methods:
# - `__init__(w: List[int])` initializes the object
# - `pickIndex()` returns a random index i with probability proportional to w[i]
#
# For example, w = [1, 3]
# → Index 0 should be picked 25% of the time
# → Index 1 should be picked 75% of the time

# 📚 Pattern: Prefix Sum + Binary Search + Random Sampling

# 🔍 Key Insight:
# Convert weights into a **prefix sum array**:
#   w = [1, 3] → prefix_sums = [1, 4]
# Randomly pick a number between 1 and total weight (inclusive).
# Use **binary search** (`bisect_left`) to find where this number fits.
#
# This maps uniform random numbers into weighted buckets efficiently.

# ✅ Time Complexity:
# - __init__: O(n)
# - pickIndex: O(log n) using binary search
# ✅ Space Complexity: O(n) — for prefix sums

import random
import bisect
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum) # random num picked btw 1 and total sum
        return bisect.bisect_left(self.prefix_sums, target)

# 🔁 Dry Run Example:
# w = [1, 3, 2]
# → prefix_sums = [1, 4, 6]
# Random number is picked in [1, 6]
# Mapped as:
#   1 → index 0
#   2, 3, 4 → index 1
#   5, 6 → index 2

# Manual Binary Search | bisect.bisect_left(self.prefix_sums, target)
# def binary_search(prefix_sums, target):
#    left, right = 0, len(prefix_sums) - 1
#    while left < right:
#        mid = (left + right) // 2
#        if prefix_sums[mid] < target:
#            left = mid + 1
#        else:
#            right = mid
#    return left

# 📌 Common Gotchas:
# - Don't use `random.randint(0, total)` — it must be 1-based to match prefix sum indexing.
# - Must use `bisect.bisect_left`, not right
# - Always build the prefix sum during `__init__` for efficiency

# 🧠 Concept Reinforced:
# - Prefix sum to map values to cumulative ranges
# - Binary search to locate which range a random number falls into
# - Efficient O(log n) weighted sampling