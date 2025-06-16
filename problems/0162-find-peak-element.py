# LeetCode 162 - Find Peak Element
# https://leetcode.com/problems/find-peak-element/

# ✅ Problem:
# A peak element is an element that is strictly greater than its neighbors.
# Return the index of any peak. Multiple correct answers are allowed.

# 🔍 Key Insight:
# We can use binary search to find a peak efficiently.
# If nums[mid] > nums[mid + 1], the peak lies on the left (including mid).
# Otherwise, it lies on the right.

# ✅ Time Complexity: O(log n) — binary search halves the search space each step
# ✅ Space Complexity: O(1) — constant extra space

# 📌 Common Gotchas:
# - Peak is not necessarily the global maximum.
# - Be careful not to access nums[mid+1] out of bounds.
# - The logic only compares to the right neighbor, not both sides.

# 📚 Pattern: Binary Search on Answer Space (not sorted order)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid  # peak is in the left half
            else:
                left = mid + 1  # peak is in the right half

        return left  # or right (same when loop exits)

# 🔁 Dry Run Example:
# Input: nums = [1, 2, 1, 3, 5, 6, 4]
#
# Step 1:
# left = 0, right = 6
# mid = 3 → nums[3] = 3 < nums[4] = 5 → go right → left = 4
#
# Step 2:
# left = 4, right = 6
# mid = 5 → nums[5] = 6 > nums[6] = 4 → go left → right = 5
#
# Step 3:
# left = 4, right = 5
# mid = 4 → nums[4] = 5 < nums[5] = 6 → go right → left = 5
#
# Exit: left = 5, right = 5 → return 5
# ✅ nums[5] = 6 is a valid peak (greater than both neighbors)

# 🔚 Final Answer: 5