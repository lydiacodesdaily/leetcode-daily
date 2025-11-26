# LeetCode 435 - Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
#
# ✅ Problem:
# Given an array of intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of intervals you need to remove to make 
# the rest of the intervals non-overlapping.
#
# 📚 Pattern:
# Greedy Algorithm (Activity Selection Problem)
#
# 🔍 Core Idea:
# - Sort intervals by END time (not start!)
# - Greedily keep intervals that end earliest → leaves most room for future intervals
# - Count overlaps: if current start < previous end, we have overlap → increment count
# - If no overlap, update the end pointer
#
# 🧠 Memory Hook:
# Sort by END → greedy: keep earliest ending
# if start >= curr_end → no overlap, update end
# else → overlap, count++
#
# ✅ Time Complexity: O(n log n) — sorting dominates
# ✅ Space Complexity: O(1) — only tracking curr_end and count
#
# 📌 Common Gotchas:
# - Must sort by END time, not start time (greedy choice)
# - Overlap check: start < curr_end (not start <= curr_end, depends on problem definition)
# - For this problem, [1,2] and [2,3] do NOT overlap (touching is okay)

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Edge case: empty or single interval
        if not intervals or len(intervals) == 1:
            return 0
        
        # Sort by end time (greedy: keep intervals that end earliest)
        intervals.sort(key=lambda x: x[1])
        
        # Initialize
        count = 0
        curr_end = float('-inf')
        
        # Iterate through sorted intervals
        for start, end in intervals:
            # No overlap: current interval starts at or after previous end
            if start >= curr_end:
                curr_end = end  # Update end pointer (keep this interval)
            else:
                # Overlap detected: need to remove this interval
                count += 1
                # curr_end stays the same (we keep the previous one with earlier end)
        
        return count


# ========================================
# DRY RUN (Interview Walkthrough)
# ========================================
"""
Example: intervals = [[1,2], [2,3], [1,3], [3,4]]

Step 1: Sort by END time
[[1,2], [2,3], [1,3], [3,4]] → [[1,2], [2,3], [1,3], [3,4]]
Wait, let me re-sort properly by end:
- [1,2] end=2
- [2,3] end=3
- [1,3] end=3
- [3,4] end=4

Sorted: [[1,2], [2,3], [1,3], [3,4]]

Step 2: Initialize
count = 0
curr_end = -inf

Step 3: Iterate

Iteration 1: [1,2]
- start=1, end=2
- 1 >= -inf? YES → No overlap
- curr_end = 2
- count = 0

Iteration 2: [2,3]
- start=2, end=3
- 2 >= 2? YES → No overlap
- curr_end = 3
- count = 0

Iteration 3: [1,3]
- start=1, end=3
- 1 >= 3? NO → Overlap!
- count = 1 (remove [1,3])
- curr_end stays 3

Iteration 4: [3,4]
- start=3, end=4
- 3 >= 3? YES → No overlap
- curr_end = 4
- count = 1

Return: 1 ✅

---

Why greedy works:
By keeping [2,3] (ends at 3) instead of [1,3] (also ends at 3),
we don't lose any opportunity. The interval that ends earliest
always leaves the most room for future intervals.

Key insight: Sorting by END time ensures we process intervals
in the order that maximizes our greedy choices.
"""