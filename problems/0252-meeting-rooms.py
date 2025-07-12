# LeetCode 252 - Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

# ✅ Problem:
# Given a list of meeting intervals, determine if a person can attend all meetings.
# Return False if any two intervals overlap.

# 📚 Pattern:
# Interval Sorting + Greedy Comparison

# 🔍 Key Insight:
# Sort intervals by start time.
# Then, for each pair of consecutive intervals, check if the current start is
# earlier than the previous end. If so, there's an overlap → return False.

# 🧠 Memory Hook:
# 🗂 Sort by start
# 📏 If cur.start < prev.end → overlap → can't attend all → return False
# ✅ Else return True

# ✅ Time: O(n log n) — for sorting
# ✅ Space: O(1) — in-place comparison, no extra data structures used

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Compare each interval with the previous one
        for i in range(1, len(intervals)):
            # If current start time is before previous end time → overlap
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        # No overlaps found
        return True

# 🔄 Dry Run Example:
# intervals = [[0,30],[5,10],[15,20]]
# Sorted: [[0,30], [5,10], [15,20]]
# 5 < 30 → overlap → return False
