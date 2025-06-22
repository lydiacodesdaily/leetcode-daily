# LeetCode 1091 - Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# ✅ Problem:
# Given an n x n binary matrix `grid`, return the length of the shortest clear path
# from top-left to bottom-right, moving in 8 directions. Return -1 if no such path exists.

# 🔍 Core Idea:
# Use BFS to explore the grid starting from (0,0).
# For each move, try all 8 directions. The first time we reach (n-1, n-1), return path length.

# 🧠 Memory Hook:
# BFS grid traversal → 8 directions  
# queue = (r, c, path_len)  
# mark visited before enqueue  
# return length on reaching (n-1, n-1)

# 📚 Pattern: BFS on Grid

# ✅ Time Complexity: O(n²) – worst case we visit all cells
# ✅ Space Complexity: O(n²) – visited matrix + queue

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 🔒 Early exit: if start or end is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        # ✅ Step 1: Define 8 directions (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        # ✅ Step 2: BFS setup → queue holds (row, col, path_length)
        queue = deque([(0, 0, 1)])  # starting from top-left with length 1

        # ✅ Step 3: Track visited to avoid cycles
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        # ✅ Step 4: Standard BFS traversal
        while queue:
            r, c, length = queue.popleft()

            # 🏁 Reached bottom-right corner
            if r == n - 1 and c == n - 1:
                return length

            # 🧭 Try all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # ✅ Within bounds, not visited, and cell is open (0)
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, length + 1))

        # ❌ No valid path
        return -1

# 🔁 Dry Run Example:
# Input: grid = [[0,1],
#                [1,0]]
#
# Start at (0,0) → enqueue (0,0,1)
# - (0,0) → (1,1) is a valid move (diagonal, not blocked) → enqueue (1,1,2)
# - (1,1) is destination → return 2

# 🔚 Final Answer: 2