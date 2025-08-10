# LeetCode 658 - Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/
#
# ✅ Problem:
# Given a sorted array arr, an integer k, and a target x,
# return the k elements closest to x, in ascending order.
# If a tie, prefer the smaller numbers.
#
# 📚 Pattern:
# Binary Search on Window (search left bound of a fixed-size window)
#
# 🔍 Core Idea:
# The answer is always a contiguous subarray of length k.
# Binary search the left index L in [0 .. n - k].
# At mid = (L+R)//2, compare the two "competing edges":
#   - a = arr[mid]          (left edge inside the window)
#   - b = arr[mid + k]      (first element right outside the window)
# If left edge is farther from x than the right-outside element,
# slide window to the right; otherwise slide left (tie → prefer left/smaller).
#
# 🧠 Memory Hook:
# "window size k → BS left bound
# compare edges: (x - a) vs (b - x)
# right closer → L = mid + 1
# else R = mid"
#
# ✅ Time Complexity: O(log(n - k) + k)
# ✅ Space Complexity: O(1) extra (ignoring output)
#
# 📌 Common Gotchas:
# - Don’t sort by |arr[i]-x| then pick k; you’ll break the ascending order rule.
# - Make sure to binary-search ONLY the left index in [0 .. n-k].
# - Tie must favor the smaller numbers → move left when equal (R = mid).
#
# 📎 Plain-sentence explanation for the key comparison (as requested):
# - arr[mid] is the left edge of the current k-length window.
# - arr[mid + k] is the first element just to the right of that window.
# - If (x - arr[mid]) > (arr[mid + k] - x), it means:
#     "The left edge is farther from x than the element just to the right."
#   → Shift the window right: left = mid + 1
# - Else:
#     "The left side is better (or equal, and we prefer smaller numbers)."
#   → Move/keep left: right = mid
#
# 🔄 Dry Run:
# arr = [1,2,3,4,5], k=4, x=3
# Search L in [0..1]
# L=0,R=1 → mid=0
#   a=arr[0]=1, b=arr[4]=5
#   x-a = 3-1 = 2
#   b-x = 5-3 = 2
#   2 > 2 ? No → R = mid = 0
# End: L=0 → arr[0:4] = [1,2,3,4] ✅ (tie favored left/smaller)
#
# --- Clean Interview Code with grouped skeletal steps ---

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - k  # search space for the left bound of size-k window

        # 🧭 Binary search the best left bound
        while left < right:
            mid = (left + right) // 2

            # Compare distances of competing edges:
            # a = arr[mid]        (left edge of window)
            # b = arr[mid + k]    (first element just to the right of the window)
            #
            # In simple words:
            # If x - arr[mid] > arr[mid + k] - x:
            #   The left edge is farther from x than the right-outside element
            #   → closer on the right → shift window right
            # else:
            #   Left side is better or equal (ties favor smaller) → move/keep left
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # 🎯 left now points to the optimal window start
        return arr[left:left + k]


# --- Embedded Example ---
# Input: arr=[1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
#
# Another:
# arr=[1,2,3,4,5,6,7], k=3, x=5.2
# L in [0..4]
# mid=2: a=3, b=6 → (5.2-3)=2.2 vs (6-5.2)=0.8 → 2.2 > 0.8 → L=3
# mid=3: a=4, b=7 → (5.2-4)=1.2 vs (7-5.2)=1.8 → 1.2 > 1.8 ? No → R=3
# L=3 → arr[3:6]=[4,5,6] ✅