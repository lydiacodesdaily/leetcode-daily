# LeetCode 1353 - Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
#
# ✅ Problem:
# You are given events where each event has [startDay, endDay].
# You can attend at most one event per day.
# Return the maximum number of events you can attend.
#
# 📚 Pattern:
# Greedy + Min-Heap (priority queue)
#
# 🔍 Core Idea:
# - Sort events by start day.
# - Simulate each day:
#     1) Push all events starting today into a min-heap keyed by endDay.
#     2) Pop expired events (end < today).
#     3) Attend the one ending soonest (pop from heap).
# - This maximizes future availability.
#
# 🧠 Memory Hook:
# - heap → end days of currently available events
# - day → simulation clock
# - i → index into sorted events list
# - total → count of attended events
#
# ✅ Time Complexity: O(n log n) [sort + heap ops]
# ✅ Space Complexity: O(n) [heap]
#
# 📌 Common Gotchas:
# - Must remove expired events each day.
# - If heap empty, jump day forward to next event start.
# - Use min-heap to always pick event with smallest endDay.

import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 1. Sort events by startDay
        events.sort()
        n = len(events)

        # 📝 Variables:
        # i: pointer into sorted events (which event to process next)
        i = 0
        # day: current simulation day
        day = 0
        # heap: min-heap storing endDays of all currently available events
        heap = []
        # total: number of events attended so far
        total = 0

        # 2. Simulate until all events considered and heap empty
        while heap or i < n:
            if not heap:
                # Jump day to next event start if heap empty
                day = events[i][0]

            # Add all events that start today into heap
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove all expired events (endDay < today)
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend event that ends earliest (greedy)
            if heap:
                heapq.heappop(heap)
                total += 1

            # Move to next day
            day += 1

        return total

# 🔄 Dry Run Example:
# Input: [[1,2],[2,3],[3,4]]
# Sorted = [[1,2],[2,3],[3,4]]
# Day 1: push [1,2], heap=[2], attend → total=1
# Day 2: push [2,3], heap=[3], attend → total=2
# Day 3: push [3,4], heap=[4], attend → total=3
# Answer = 3 ✅