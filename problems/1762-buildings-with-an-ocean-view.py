# LeetCode 1762 - Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/

# ✅ Problem:
# Given an array `heights` representing building heights from left to right,
# return the indices of the buildings with an ocean view (ocean is to the right).
# A building has an ocean view if all buildings to its right are shorter.

# 🔍 Key Insight:
# Scan from right to left while tracking the max height seen so far.
# A building has an ocean view if its height is strictly greater than all buildings to its right.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) (excluding output)

from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = float('-inf')

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]

        return res[::-1]  # Reverse to return indices in left-to-right order

# 🔁 Dry Run Example:
# Input: heights = [4, 2, 3, 1]
# Traverse from right to left:
# i = 3 → 1 > -inf → ✅ res = [3], max_height = 1
# i = 2 → 3 > 1    → ✅ res = [3, 2], max_height = 3
# i = 1 → 2 > 3    → ❌ skip
# i = 0 → 4 > 3    → ✅ res = [3, 2, 0], max_height = 4
# Final result = [0, 2, 3]

# 📌 Common Gotchas:
# - Remember to reverse the result at the end.
# - Use `>` not `>=` (must be strictly taller than buildings to the right).
# - Right-to-left traversal simplifies the logic greatly.

# 📚 Pattern: Monotonic Scan (Right-to-Left Max Tracking)