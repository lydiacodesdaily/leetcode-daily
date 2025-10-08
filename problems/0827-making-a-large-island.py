# LeetCode 827 - Making A Large Island
# https://leetcode.com/problems/making-a-large-island/

# ✅ Problem:
# You are given an n x n binary matrix grid. You may flip at most one 0 → 1.
# Return the size of the largest island possible after one flip.
# An island is a 4-directionally connected group of 1s.

# 🔍 Key Insight:
# - First, use DFS to label each island with a unique ID (starting from 2).
# - Track the area (number of cells) of each island ID in a map.
# - Then, for each 0 cell, try flipping it to 1 and compute the area by summing neighboring island IDs (no duplicates).
# - The final answer is the max area found this way, or the max of existing islands.

# 📚 Pattern: DFS + Island Labeling + HashMap

# ✅ Time Complexity: O(n^2) — we visit each cell a constant number of times.
# ✅ Space Complexity: O(n^2) — for visited labels and island area map.

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        area = {}  # Map island_id → area size

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1️⃣: DFS to label each island with an ID and record its area
        def dfs(r: int, c: int, id: int) -> int:
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id  # Mark with island ID
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, id)
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # Step 2️⃣: Check each 0-cell to see max area possible by flipping it
        max_area = max(area.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_area = 1  # count the flipped cell
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            id = grid[nr][nc] # stores seen island_id
                            if id > 1 and id not in seen:
                                new_area += area[id]
                                seen.add(id)
                    max_area = max(max_area, new_area)

        return max_area if max_area else n * n  # handle case: all 1s

# 🔁 Dry Run:
# Input: [[1, 0], [0, 1]]
# Step 1: DFS labels → [[2, 0], [0, 3]], area = {2:1, 3:1}
# Try flipping (0,1) → connects island 2 and 3 → area = 1 (flipped) + 1 + 1 = 3
# Output: 3

# 📌 Common Gotchas:
# - Remember to skip duplicate neighbors by checking `seen`
# - Don’t flip unless `grid[r][c] == 0`
# - Edge case: grid already all 1s → return n * n

"""
grid (after Step 1 labeling):
2 0
0 3
area = {2:1, 3:1}

Try flip (0,1):
  neighbors: (0,0)=2, (1,1)=3 → distinct islands {2,3}
  new_area = 1 (flipped) + area[2]=1 + area[3]=1 = 3
max_area = 3

Any other flip gives at most 2 here. Final = 3.
"""