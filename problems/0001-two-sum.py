# LeetCode 1 - Two Sum
# https://leetcode.com/problems/two-sum/

# ✅ Problem:
# Given an array of integers `nums` and an integer `target`,
# return indices of the two numbers such that they add up to `target`.

# You may assume that each input has exactly one solution,
# and you may not use the same element twice.

# 🧠 Memory Hook:
# for each num → check if (target - num) is in map
# if found → return [map[complement], i]
# else → store num:index in map

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps value → index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

"""
nums = [2, 7, 11, 15], target = 9

i = 0 → num = 2 → complement = 7 → not in map → store 2:0
i = 1 → num = 7 → complement = 2 → ✅ found in map
→ return [0, 1]
"""