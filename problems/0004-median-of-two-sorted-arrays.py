# LeetCode 4 - Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# ✅ Problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays. The overall run time complexity should be O(log(min(m, n))).

# 🧩 Pattern:
# Binary Search on Partition Index

# 🧠 Memory Hook:
# binary search on smaller array
# partition A + B = (total_len + 1) // 2
# ensure max(left) ≤ min(right)
# if wrong: move partition left/right
# odd → median = max(lefts), even → avg of max(lefts) & min(rights)

# ✅ Time Complexity: O(log(min(m, n)))
# ✅ Space Complexity: O(1)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half = (total_len + 1) // 2

        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1

            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if total_len % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = partition1 - 1  # Move left
            else:
                left = partition1 + 1   # Move right

        raise ValueError("Input arrays are not sorted or invalid")

# 🔁 Example Dry Run:
# nums1 = [1, 3], nums2 = [2]
# Combined sorted = [1, 2, 3] → median = 2
