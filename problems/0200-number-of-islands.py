# LeetCode 200 - Number of Islands
# https://leetcode.com/problems/number-of-islands/

# ✅ Problem:
# Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. Return the number of distinct islands.

# 📚 Pattern:
# Grid Traversal (DFS) — Flood Fill / "Burn the island"

# 🔍 Key Insight:
# - Traverse each cell in the grid
# - When we find '1', it's a new island → increment count
# - Use DFS to mark all connected '1's as '0' to avoid recounting

# 🧠 Memory Hook:
# for r, c in grid:
#   if grid[r][c] == '1':
#       count += 1
#       dfs(r, c)  # burn entire island (set all 1s to 0)

# ✅ Time Complexity: O(m * n) — visit every cell once
# ✅ Space Complexity: O(m * n) worst-case recursion stack (DFS)

# 📌 Common Gotchas:
# - Must visit **all 4 directions** (no diagonals)
# - Remember to **mark visited** inside DFS to avoid infinite recursion
# - Mutate grid in-place by setting '1' → '0'

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int):
            # ✅ Bounds and base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return

            # 🔥 Mark as visited (burn the land)
            grid[r][c] = '0'

            # ⬆️⬇️⬅️➡️ Visit 4 directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # 🌍 Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count

# 🔄 Dry Run Example:
# Input:
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# Output: 3
# Explanation:
# - First island: top-left cluster → burned in one DFS
# - Second island: middle (2,2)
# - Third island: bottom-right cluster