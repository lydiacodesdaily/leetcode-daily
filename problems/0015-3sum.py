# LeetCode 15 - 3Sum
# https://leetcode.com/problems/3sum/

# ✅ Problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.

# 📚 Pattern: Two Pointers + Sorting

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(1) (excluding output)

# 🧠 Memory Hook:
# sort first to group duplicates
# fix first → two-pointer scan for rest
# skip dup i, skip dup left/right if same as prev

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate 'i' values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

# 🔍 Example:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Sorted: [-4, -1, -1, 0, 1, 2]
# Output: [[-1, -1, 2], [-1, 0, 1]]

# 🧪 Dry Run:
# i = 0 → -4 → left=1, right=5 → sum = -3 → left++
# i = 1 → -1 → left=2, right=5 → sum = 0 → ✅ append, skip duplicates
# i = 2 → skip (same as prev i)
# i = 3 → 0 → left=4, right=5 → sum = 3 → right--
