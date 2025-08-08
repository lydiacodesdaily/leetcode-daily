# LeetCode 852 - Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
#
# ✅ Problem:
# Given a mountain array arr (strictly up, then strictly down), return the index of the peak.
#
# 📚 Pattern:
# Binary Search on "slope" (bitonic peak)
#
# 🔍 Core Idea:
# Compare arr[mid] vs arr[mid + 1]:
# - If arr[mid] < arr[mid + 1], we are on the **increasing** slope → peak is to the **right** (l = mid + 1)
# - Else, we are on the **decreasing** slope or at peak → peak is at **mid or left** (r = mid)
#
# 🧠 Memory Hook:
# mid < mid+1 → go right
# mid >= mid+1 → go left (keep mid)
# stop when l == r → peak index
#
# ✅ Time Complexity: O(log n)
# ✅ Space Complexity: O(1)
# ✅ NOT a DP problem → safe for E5 full‑stack
#
# 📌 Common Gotchas:
# - Use while l < r with r = mid (not mid-1) to keep the candidate peak
# - Always read arr[mid + 1], so compute mid so that mid + 1 is in-bounds
# - Array length ≥ 3 and guaranteed mountain per problem statement

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        # Invariant: peak ∈ [l, r]
        while l < r:
            mid = (l + r) // 2
            # Compare to the next element to detect slope direction
            if arr[mid] < arr[mid + 1]:
                # Increasing slope → peak is strictly to the right
                l = mid + 1
            else:
                # Decreasing slope (or at peak) → keep mid in the range
                r = mid
        return l  # or r; they are equal

# 🔄 Dry Run:
# arr = [0, 2, 5, 3, 1]
# l=0, r=4
# mid=2 → arr[2]=5, arr[3]=3 → 5 >= 3 → r=2
# l=0, r=2
# mid=1 → arr[1]=2, arr[2]=5 → 2 < 5 → l=2
# l=2, r=2 → return 2 ✅

# 🧪 Example:
# print(Solution().peakIndexInMountainArray([0,1,0]))          # 1
# print(Solution().peakIndexInMountainArray([0,2,5,3,1]))      # 2
# print(Solution().peakIndexInMountainArray([3,4,5,1]))        # 2