# LeetCode 540 - Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

# ✅ Pattern:
# Binary Search on index parity

# 🔍 Key Insight:
# - Pairs straddle (even, odd) indices before the single.
# - After the single, pairing shifts to (odd, even).
# - Force mid to even; compare nums[mid] with nums[mid+1] to decide the side.

# 🧠 Memory Hook:
# "Make mid even → equal means go right, else go left"

# ✅ Time: O(log n) | ✅ Space: O(1)

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1:
                mid -= 1  # ensure mid is even

            if nums[mid] == nums[mid + 1]:
                # Proper pair at (mid, mid+1) → single is to the right
                lo = mid + 2
            else:
                # Pair broken at mid → single is at mid or to the left
                hi = mid
        return nums[lo]