# Leetcode 986 - Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

# ✅ Problem:
# Given two lists of non-overlapping intervals sorted by start time,
# return the list of their intersections.

# 📚 Pattern: Two Pointers over Sorted Intervals
# 🧪 Subtype: Overlap Detection using max(start), min(end)

# 🧠 Memory Hook:
# overlap if max(start) ≤ min(end)
# move pointer of interval that ends first
# add [max(start), min(end)] if valid

# ✅ Time: O(m + n)
# ✅ Space: O(1) extra, O(k) for result

from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0

        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]

            # Calculate potential overlap
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                res.append([start, end])

            # Move the pointer with the smaller end
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return res

# 🔄 Dry Run:
# A = [[0,2],[5,10],[13,23],[24,25]]
# B = [[1,5],[8,12],[15,24],[25,26]]
#
# Intersections:
# [1,2], [5,5], [8,10], [15,23], [24,24], [25,25] ✅
