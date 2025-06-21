# LeetCode 56 - Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# ✅ Problem:
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals and return an array of the non-overlapping intervals
# that cover all the intervals in the input.

# 📚 Pattern:
# Sorting + Merging Intervals

# 🔍 Core Idea:
# - Sort intervals by start time.
# - Compare each interval with the last interval in result list:
#   → If they overlap, merge them.
#   → If not, add the interval as is.

# 🧠 Memory Hook:
# sort by start
# if new_start <= last_end → merge
# else → append as new group

# ✅ Time Complexity: O(n log n) – for sorting
# ✅ Space Complexity: O(n) – for output list

# 📌 Common Gotchas:
# - Sorting must be by start time, not end time
# - Check for overlap with last interval using `start <= prev_end`
# - Don’t forget to initialize result with the first interval

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 🧭 Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # 🧭 Step 2: Initialize result with first interval
        merged = [intervals[0]]

        # 🧭 Step 3: Iterate through intervals and merge if overlapping
        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                # Overlapping → merge with last interval
                merged[-1][1] = max(last_end, end)
            else:
                # No overlap → add as a new interval
                merged.append([start, end])

        return merged

# 🔄 Dry Run:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# After sorting: [[1,3],[2,6],[8,10],[15,18]]
# Step 1: merged = [[1,3]]
# → [2,6] overlaps → merge → [[1,6]]
# → [8,10] no overlap → append → [[1,6],[8,10]]
# → [15,18] no overlap → append → [[1,6],[8,10],[15,18]]
# ✅ Output: [[1,6],[8,10],[15,18]]