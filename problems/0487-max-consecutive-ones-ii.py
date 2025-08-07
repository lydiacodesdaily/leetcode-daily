# 🔁 Part 2: Variant — Max Consecutive 1s with At Most One 0 Flipped
# LeetCode 487 - Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/

# ✅ Problem:
# Flip at most one 0 to 1. Return longest streak of 1s possible.

# 📚 Pattern:
# Sliding Window with Zero Counter

# 🔍 Key Insight:
# - Keep a sliding window where at most one 0 is allowed
# - When we exceed 1 zero, move the left pointer forward until we're back in a valid state

# 🧠 Memory Hook:
# window with at most one zero
# if more than one 0 → shrink left

# ✅ Time: O(n)
# ✅ Space: O(1)

class Solution:
    def findMaxConsecutiveOnesWithOneFlip(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # shrink window

            max_len = max(max_len, right - left + 1)

        return max_len


# 🔍 Edge Case Examples:

"""
Example 1:
Input: [1,1,0,1,1,1]
Output: 3  → original problem

Example 2:
Input: [1,0,1,1,0]
Original → max = 2
Flipped → max = 4 (flip 1st 0 or 2nd 0)

Example 3:
Input: [0,0,0]
Original → max = 1
Flipped → max = 1 (flip one 0)

Example 4:
Input: [1,1,1,1]
Output: 4 for both versions

Example 5:
Input: []
Output: 0
"""