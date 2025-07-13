# LeetCode 253 - Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

# ✅ Problem:
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...],
# return the minimum number of conference rooms required.

# 📚 Pattern:
# Greedy + Min Heap (Priority Queue)

# 🔍 Key Insight:
# - Sort meetings by start time
# - Use a min-heap to track the earliest ending meeting
# - If a meeting starts after the earliest ending one → reuse room (pop heap)
# - Otherwise → allocate a new room (push end to heap)
# - Max size of the heap = min number of rooms needed

# 🧠 Memory Hook:
# 📅 Sort by start
# 🧺 Min-heap for end times
# 🧼 start >= min_end → pop heap (reuse room)
# 🧱 start < min_end → push new end (need room)
# ✅ return len(heap)

# ✅ Time: O(n log n) — due to sorting and heap operations
# ✅ Space: O(n) — heap may store all meetings in worst case

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Min-heap to store end times of meetings currently using a room
        min_heap = [intervals[0][1]]

        # Step 3: Iterate through remaining intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # If current meeting starts after earliest ending meeting → reuse room
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Add current meeting's end time to heap (new or reused room)
            heapq.heappush(min_heap, end)

        # Step 4: Number of meeting rooms = size of the heap
        return len(min_heap)

# 🔄 Dry Run Example:
# Input: [[0,30],[5,10],[15,20]]
# Sorted: [[0,30],[5,10],[15,20]]
# Heap = [30]
# → Add 10 → [10,30]
# → 15 >= 10 → pop 10, push 20 → [20,30]
# → Final heap size = 2 → return 2