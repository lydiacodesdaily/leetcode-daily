# LeetCode 934 - Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/

# ✅ Problem:
# You are given a binary grid with two islands (groups of 1s).
# You may flip 0s into 1s to connect the two islands.
# Return the **minimum number of 0s** you must flip to connect them.

# 📚 Pattern:
# DFS + BFS Combo (Multi-source BFS from 1st island)

# 🔍 Key Insight:
# - First island: use DFS to find and mark it, and store its coordinates.
# - Use BFS starting from all positions of the first island to reach the second.
# - Each BFS level = number of 0s flipped so far (bridge length).

# 🧠 Memory Hook:
# Step 1: DFS → mark first island + queue its coordinates
# Step 2: BFS → expand outward to find second island (grid[r][c] == 1)
# First time we reach second island → return BFS level

# ✅ Time Complexity: O(n²)
# ✅ Space Complexity: O(n²)

# 📌 Common Gotchas:
# - Don’t stop DFS after one cell; mark all connected 1s
# - Must add *all* island-1 cells to BFS queue
# - Mark visited immediately in BFS to prevent repeats

from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        queue = deque()

        # -----------------------------
        # ✅ Step 1: DFS to mark 1st island and collect border
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < n):
                return
            if visited[r][c] or grid[r][c] == 0:
                return
            visited[r][c] = True
            queue.append((r, c))  # Add for BFS later
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r + dr, c + dc)

        # 🔍 Find first island
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # -----------------------------
        # ✅ Step 2: BFS to find shortest path to second island
        level = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            return level  # ✅ Found second island
                        queue.append((nr, nc))
                        visited[nr][nc] = True  # ✅ Mark visited immediately
            level += 1