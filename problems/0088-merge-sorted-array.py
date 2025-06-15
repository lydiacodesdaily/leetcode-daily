# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

"""
🧠 Pattern: Two Pointers (Back to Front)
🎯 Problem: Merge two sorted arrays in-place — nums1 and nums2.
📌 Constraints:
- nums1 has size m + n; only first m elements are valid
- nums2 has n elements
- Merge nums2 into nums1 so the result is sorted

⏰ Time Complexity: O(m + n)
📦 Space Complexity: O(1) — in-place

Why this works:
- Start filling from the back (index m + n - 1) to avoid overwriting nums1's valid values.
"""

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