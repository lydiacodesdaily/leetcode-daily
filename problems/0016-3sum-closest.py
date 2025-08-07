# LeetCode 16 - 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# ✅ Problem:
# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input has exactly one solution.

# 📚 Pattern:
# Two Pointers after Sorting

# 🔍 Key Insight:
# - Similar to 3Sum, but instead of finding all triplets summing to target,
#   we track the triplet whose sum is *closest* to target.
# - Use two-pointer pattern with `abs(total - target)` comparison.

# 🧠 Memory Hook:
# - sort array
# - fix i, use two pointers
# - update `closest_sum` if `abs(total - target)` is smaller

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(1)

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # ✅ If closer to target, update closest_sum
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # Exact match!

        return closest_sum

# 🔄 Dry Run:
# Input: nums = [-1, 2, 1, -4], target = 1
# Sorted: [-4, -1, 1, 2]
# Try combinations:
#   -4 + -1 + 2 = -3 → diff = 4
#   -4 + 1 + 2 = -1 → diff = 2
#   -1 + 1 + 2 = 2  → diff = 1 ✅ closest so far
# Final answer = 2