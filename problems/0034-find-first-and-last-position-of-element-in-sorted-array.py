# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# ✅ Problem:
# Given an array of integers sorted in ascending order and a target value,
# find the first and last position of the target.
# If the target is not found, return [-1, -1].

# 📚 Pattern:
# Binary Search (Modified Bound Search)
# - First binary search to find the **left bound**
# - Second binary search to find the **right bound**

# ✅ Time Complexity: O(log n) - binary search twice
# ✅ Space Complexity: O(1)

# 🧠 Memory Hook:
# binary search twice: once for first occurrence, once for last
# if nums[mid] == target → store result, keep searching left/right
# if is_first → move right = mid - 1
# if not is_first → move left = mid + 1

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
                    # Keep searching left or right depending on bound
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        return [find_bound(True), find_bound(False)]

"""
🧪 Example Test Cases:

nums = [5,7,7,8,8,10], target = 8
# Output: [3, 4]

nums = [5,7,7,8,8,10], target = 6
# Output: [-1, -1]

nums = [], target = 0
# Output: [-1, -1]

nums = [1], target = 1
# Output: [0, 0]

nums = [2, 2], target = 2
# Output: [0, 1]
"""
# 🔍 Example:
# nums = [5,7,7,8,8,10], target = 8
# First bound: index 3
# Last bound: index 4
# Output: [3, 4] ✅
