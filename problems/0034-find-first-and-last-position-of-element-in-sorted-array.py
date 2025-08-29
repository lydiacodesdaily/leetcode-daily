# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# ✅ Problem:
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# 📚 Pattern:
# Binary Search

# 🔍 Core Idea:
# Perform two binary searches:
# - First to find the leftmost (first) occurrence of the target.
# - Second to find the rightmost (last) occurrence of the target.
# Search space is reduced by focusing on left or right boundaries even after finding the target.

# 🧠 Memory Hook:
# run two binary searches:
# - search for first → if found, keep searching left
# - search for last → if found, keep searching right
# return [first, last]

# ✅ Time Complexity: O(log n) — two binary searches
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Make sure to keep searching even after finding target (continue left/right)
# - Handle edge cases when target is not found

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid
                    if is_first:
                        right = mid - 1  # Keep searching left
                    else:
                        left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        return [find_bound(True), find_bound(False)]

# 🔄 Dry Run:
# Input: nums = [5,7,7,8,8,10], target = 8
# First search (find leftmost):
# → find_bound(True) returns 3
# Second search (find rightmost):
# → find_bound(False) returns 4
# Final answer: [3, 4]