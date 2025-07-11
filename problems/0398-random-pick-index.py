# LeetCode 398 - Random Pick Index
# https://leetcode.com/problems/random-pick-index/

# ✅ Problem:
# Given an integer array nums, implement a class that randomly returns
# an index of the given target number. All target indices should have equal probability.

# 📚 Pattern:
# Hash Map (Preprocessing)

# 🔍 Key Insight:
# - Preprocess: map each number to all its indices
# - Then we can return a random index in O(1) time using random.choice

# 🧠 Memory Hook:
# preprocess → map num to indices → pick = random.choice(map[num])

# ✅ Time Complexity:
# - __init__: O(n)
# - pick(): O(1)

# ✅ Space Complexity: O(n) for storing the map

import random
from collections import defaultdict
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.index_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_map[target])


# 🔄 Example usage:
# Input: nums = [1, 2, 3, 3, 3]
# pick(3) should randomly return index 2, 3, or 4

if __name__ == "__main__":
    sol = Solution([1, 2, 3, 3, 3])
    print("Random pick for 3:", [sol.pick(3) for _ in range(10)])