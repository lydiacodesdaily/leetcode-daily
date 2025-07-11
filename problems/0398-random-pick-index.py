# LeetCode 398 - Random Pick Index
# https://leetcode.com/problems/random-pick-index/

# ✅ Problem:
# Given an integer array nums, implement a class that allows you to
# pick a random index for a given target value, where each matching index
# has an equal probability of being chosen.

# 📚 Pattern:
# Reservoir Sampling

# 🔍 Key Insight:
# - We want to pick a random index from many potential matches without storing them all.
# - Reservoir Sampling (size 1) lets us do this in O(n) time and O(1) space.

# ✅ Time Complexity: O(n) per pick
# ✅ Space Complexity: O(1) extra (excluding input list)

import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = -1
        count = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1

                # 🎯 KEY IDEA (Reservoir Sampling):
                # We generate a random number between 1 and `count`.
                # If that number is 1, we choose the current index as the new result.
                # Probability of choosing current index = 1/count
                # This ensures that each occurrence of the target has equal chance
                # of being picked by the time the loop ends.
                if random.randint(1, count) == 1:
                    result = i

        return result


# 🔄 Example:
# nums = [1, 2, 3, 3, 3]
# pick(3) → should randomly return one of the indices [2, 3, 4] with equal probability

if __name__ == "__main__":
    sol = Solution([1, 2, 3, 3, 3])
    results = [sol.pick(3) for _ in range(10)]
    print("Random picks for target 3:", results)