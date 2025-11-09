# LeetCode 452 - Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#
# ✅ Problem:
# Given an array of balloons where points[i] = [x_start, x_end] represents a balloon
# whose horizontal diameter stretches from x_start to x_end (inclusive),
# return the minimum number of arrows needed to burst all balloons.
# An arrow shot at x bursts all balloons where x_start <= x <= x_end.
#
# 📚 Pattern:
# Greedy Algorithm (Interval Scheduling / Activity Selection variant)
#
# 🔍 Core Idea:
# - Sort balloons by END position (greedy: shoot at earliest ending position)
# - Shoot an arrow at the end of the first balloon
# - For each subsequent balloon: if it starts after current arrow position,
#   we need a new arrow (update arrow position to this balloon's end)
# - If balloon overlaps with current arrow position, it gets burst automatically
#
# 🧠 Memory Hook:
# Sort by END → shoot arrow at curr_end
# if start > curr_end → need new arrow, arrows++
# else → overlaps, same arrow bursts it
#
# ✅ Time Complexity: O(n log n) — sorting dominates
# ✅ Space Complexity: O(1) — only tracking arrow position and count
#
# 📌 Common Gotchas:
# - Must sort by END position (not start)
# - Overlap check: start > curr_end means NO overlap (need new arrow)
# - curr_end doesn't update till we add a new arrow
# - Note: start <= curr_end means overlap (inclusive on both ends!)
# - Similar to Non-overlapping Intervals but counting KEPT intervals, not removed

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Edge case: empty array
        if not points:
            return 0
        
        # Sort by end position (greedy: shoot at earliest ending position)
        points.sort(key=lambda x: x[1])
        
        # Initialize: shoot first arrow at the end of first balloon
        arrows = 1
        curr_arrow_pos = points[0][1]
        
        # Iterate through sorted balloons
        for start, end in points[1:]:
            # No overlap: balloon starts after current arrow position
            if start > curr_arrow_pos:
                # Need a new arrow
                arrows += 1
                curr_arrow_pos = end  # Shoot at the end of this balloon
            # else: balloon overlaps with current arrow → already burst
        
        return arrows


# ========================================
# DRY RUN (Interview Walkthrough)
# ========================================
"""
Example: points = [[10,16], [2,8], [1,6], [7,12]]

Step 1: Sort by END position
- [10,16] end=16
- [2,8] end=8
- [1,6] end=6
- [7,12] end=12

Sorted: [[1,6], [2,8], [7,12], [10,16]]

Step 2: Initialize
arrows = 1 (shoot first arrow)
curr_arrow_pos = 6 (shoot at end of first balloon [1,6])

Step 3: Iterate (starting from index 1)

Iteration 1: [2,8]
- start=2, end=8
- 2 > 6? NO → Overlaps!
- Balloon [2,8] contains position 6, so it gets burst by same arrow
- arrows = 1
- curr_arrow_pos = 6 (stays the same)

Iteration 2: [7,12]
- start=7, end=12
- 7 > 6? YES → No overlap!
- Need new arrow
- arrows = 2
- curr_arrow_pos = 12 (shoot at end of [7,12])

Iteration 3: [10,16]
- start=10, end=16
- 10 > 12? NO → Overlaps!
- Balloon [10,16] contains position 12, so it gets burst by arrow at 12
- arrows = 2
- curr_arrow_pos = 12 (stays the same)

Return: 2 ✅

---

Visual representation:
Balloons:  [1---6]
           [2-----8]
              [7------12]
                 [10--------16]

Arrows:         ↓ (at 6)      ↓ (at 12)

Arrow at 6 bursts: [1,6] and [2,8]
Arrow at 12 bursts: [7,12] and [10,16]
Total: 2 arrows

---

Why greedy works:
By shooting at the END of each balloon group, we maximize the chance
that future balloons will overlap with this arrow position.

Sorting by END ensures we always shoot at the earliest possible position
that bursts the current balloon, giving us the best chance to hit future ones.

Key insight: This is the OPPOSITE of Non-overlapping Intervals!
- Non-overlapping: count how many to REMOVE
- This problem: count how many to KEEP (groups of overlapping balloons)
"""