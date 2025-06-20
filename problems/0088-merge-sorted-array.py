# LeetCode 88 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# ✅ Problem:
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# nums1 has a length of m + n, where the last n elements are 0 and should be ignored.
# Modify nums1 in-place.

# 📚 Pattern: Two Pointers (Reverse Merge)

# 🧠 Memory Hook:
# merge from end → use empty slots at end of nums1
# p1 = end of nums1's real data, p2 = end of nums2
# compare & insert largest → move backward
# only loop until p2 < 0 (nums1 already in place)

# ✅ Time Complexity: O(m + n)
# ✅ Space Complexity: O(1) — in-place

# 🔍 Key Insight:
# Start filling nums1 from the back to avoid overwriting its own elements

# 📌 Common Gotchas:
# - Don’t overthink edge cases when nums1 has zeros at the end
# - No need to copy remaining nums1 values; they’re already in place
# - Only loop while p2 >= 0

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # Pointer for nums1's last valid element
        p2 = n - 1  # Pointer for nums2's last element
        p = m + n - 1  # Pointer for placement in nums1

        # Merge from the end to avoid overwriting
        while p2 >= 0: # only need to check nums2, because leftover nums1 is already in place
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

"""
🧪 Example Test Cases:

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# After merge: [1,2,2,3,5,6]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
# After merge: [1]

nums1 = [1]
m = 1
nums2 = []
n = 0
# After merge: [1]
"""