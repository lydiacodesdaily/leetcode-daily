# LeetCode 56 - Merge Intervals
# ✅ Problem: https://leetcode.com/problems/merge-intervals/
# 
# 🧩 Goal: Merge all overlapping intervals in a list.
# 
# 📦 Time Complexity: O(n log n) — due to sorting
# 📦 Space Complexity: O(n) — for the output list
#
# 📌 Use Case:
#   Useful when processing ranges, time blocks, or combining intervals.
#   Common in calendar apps, event scheduling, memory compaction, etc.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 🧱 Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        merged = []  # Final merged list

        # 🧱 Step 2: Iterate through sorted intervals
        for interval in intervals:
            # 🔍 Case 1: First interval or no overlap with last merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 🔁 Case 2: Overlapping — merge by updating end
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# 🧪 Example Dry Run:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# After sorting: [[1,3],[2,6],[8,10],[15,18]]
# Merging:
#   [1,3] + [2,6] => [1,6]
#   [1,6] + [8,10] => no overlap → add [8,10]
#   [8,10] + [15,18] => no overlap → add [15,18]
# Output: [[1,6],[8,10],[15,18]]
