# LeetCode 1091 - Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# ✅ Problem:
# Find the shortest path from the top-left to bottom-right in a binary matrix.
# You can move in 8 directions. Cells with 1 are blocked, 0 are walkable.
# Return the number of steps in the shortest path, or -1 if not possible.

# 🔍 Key Insight:
# This is a classic grid shortest path problem → use **Breadth-First Search (BFS)**.
# BFS ensures the shortest path is found by exploring level by level.

# ✅ Time Complexity: O(n²) — worst case visits all cells once
# ✅ Space Complexity: O(n²) — for visited matrix and queue

# 📌 Common Gotchas:
# - Check if the starting or ending cell is blocked
# - Use 8-directional movement (diagonals included)
# - Mark cells as visited immediately after enqueue to avoid revisits

# 📚 Pattern: BFS in 2D Grid

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # early exit if start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while queue:
            r, c, length = queue.popleft()
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, length + 1))

        return -1

# 🔁 Dry Run Example:
# Input: grid = [[0,1],
#                [1,0]]
#
# Start at (0,0) → enqueue (0,0,1)
# - (0,0) → (1,1) is a valid move (diagonal, not blocked) → enqueue (1,1,2)
# - (1,1) is destination → return 2

# 🔚 Final Answer: 2