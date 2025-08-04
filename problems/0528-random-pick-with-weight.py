# LeetCode 528 - Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

# ✅ Problem:
# Given a list of positive integers `w`, where w[i] is the weight of index i,
# implement a method pickIndex() that returns an index i with probability:
#     w[i] / sum(w)

# 📚 Pattern:
# Prefix Sum + Binary Search

# 🔍 Key Insight:
# Stretch each index into a proportional range based on weight.
# Generate a random number in [1, total], then use binary search to locate which index it maps to.

# 🧠 Memory Hook:
# "the higher the weight, the higher the chance it gets picked"
# → prefix sum turns weights into segments
# → random.randint chooses a point in that range
# → bisect_left finds which segment it falls into

# ✅ Time Complexity:
# - Constructor: O(n)
# - pickIndex(): O(log n)
# ✅ Space Complexity: O(n)

import random
import bisect
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [] #  weights into segments
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total  # total sum of weights

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)  # chooses a point in that range
        # Find the first index where prefix[i] >= target
        return bisect.bisect_left(self.prefix, target) #  bisect_left finds which segment it falls into

# 🔄 Dry Run:
# Input: w = [1, 3, 2]
# prefix = [1, 4, 6]
# total = 6
# Random target = 5 → falls into index 2 (because 4 < 5 <= 6)
# Random target = 2 → falls into index 1 (because 1 < 2 <= 4)

# So:
# index 0 = 1/6 chance
# index 1 = 3/6 chance
# index 2 = 2/6 chance