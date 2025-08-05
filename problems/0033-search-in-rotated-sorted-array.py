# LeetCode 33 - Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# ✅ Problem:
# Given a rotated sorted array (no duplicates), and a target value,
# return the index of the target if found, else return -1.

# 📚 Pattern:
# Modified Binary Search

# 🔍 Key Insight:
# At each step of binary search, either the left half OR right half is guaranteed to be sorted.
# You can check if the target lies within the sorted portion and shrink your search space accordingly.

# 🧠 Memory Hook:
# if nums[left] <= nums[mid]:  # left side sorted
#     if target in [left, mid]: right = mid - 1
# else:                        # right side sorted
#     if target in [mid, right]: left = mid + 1

# ✅ Time Complexity: O(log n) — binary search
# ✅ Space Complexity: O(1) — constant extra space

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target in left
                else:
                    left = mid + 1   # target in right
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target in right
                else:
                    right = mid - 1  # target in left

        return -1

# 🔄 Dry Run:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# mid = 3 → nums[3] = 7 → left part [4,5,6,7] is sorted
# 0 < 7, but 0 < 4 → target NOT in left → search right
# mid = 5 → nums[5] = 1 → right part [1,2] is sorted
# 0 < 1 → move right to mid - 1
# mid = 4 → nums[4] = 0 → ✅ found

# Output: 4