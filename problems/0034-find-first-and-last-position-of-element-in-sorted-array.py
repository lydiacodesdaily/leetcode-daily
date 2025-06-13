# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
🧠 Pattern: Binary Search (Lower/Upper Bound)
🎯 Problem: Return the starting and ending position of a given target value in a sorted array.
📌 Constraints:
- Array is non-decreasing (sorted)
- Must run in O(log n) time

⏰ Time Complexity: O(log n)
📦 Space Complexity: O(1)
"""

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