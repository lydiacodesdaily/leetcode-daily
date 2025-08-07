# LeetCode 485 - Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

# ✅ Part 1: Original Problem
# Given a binary array `nums`, return the max number of consecutive 1s.

# 📚 Pattern:
# Basic Linear Scan (Count + Reset)

# 🔍 Key Insight:
# - Track streak of 1s
# - Reset on 0
# - Update max at every step

# ✅ Time: O(n)
# ✅ Space: O(1)

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0  # reset on 0

        return max_count
