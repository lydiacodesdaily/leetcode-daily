# LeetCode 994 - Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/

"""
✅ Problem:
You are given an m x n grid where:
  - 0 = empty cell
  - 1 = fresh orange
  - 2 = rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten one becomes rotten.
Return the minimum number of minutes until no cell has a fresh orange.
If impossible, return -1.

📚 Pattern:
Grid BFS (multi-source)

🔍 Key Insight:
- Start BFS from *all* initially rotten oranges (multi-source BFS).
- Each BFS level = 1 minute.
- Keep track of fresh oranges count — stop when all rotten or BFS ends.
- ❌ Why DFS Fails: DFS explores depth-first, but rotting happens simultaneously in all directions (level by level) 

🧠 Memory Hook:
"Multi-source BFS = spread from all rotters at once"
(Level order traversal for time steps)

✅ Time Complexity: O(m * n) — each cell visited once
✅ Space Complexity: O(m * n) — queue + visited set
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1️⃣ Collect initial state
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # rotten
                    q.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:  # fresh
                    fresh += 1

        # 2️⃣ BFS from all rotten oranges
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, minutes = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # mark as rotten
                    fresh -= 1
                    q.append((nr, nc, minutes + 1))

        # 3️⃣ Check if all fresh oranges are gone
        return minutes if fresh == 0 else -1


"""
🔄 Dry Run Example:
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

Step 1: Initial queue = [(0,0,0)] (only rotten at (0,0)), fresh = 7
Step 2: BFS:
    - Minute 0: rot (0,1), (1,0) → fresh=5
    - Minute 1: rot (0,2), (1,1) → fresh=3
    - Minute 2: rot (2,1) → fresh=2
    - Minute 3: rot (2,2) → fresh=1
    - Minute 4: rot (1,2) → fresh=0
End: minutes=4, fresh=0 → return 4
"""

# LeetCode 994 - Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
#
# ✅ Pattern:
# BFS in a Grid (Multi-source BFS)
#
# 🔍 Key Insight:
# - All initially rotten oranges rot their adjacent fresh oranges at the same time.
# - This is a classic **multi-source BFS**: enqueue all rotten oranges first, then spread in layers.
# - Track time by counting BFS levels.
#
# 🧠 Memory Hook:
# "Start with all rotten in queue → BFS level = minutes passed → Spread until no fresh left"
#
# ✅ Time Complexity: O(m * n) — each cell is processed at most once
# ✅ Space Complexity: O(m * n) — for the BFS queue
#
# 📌 Edge Cases:
# 1. No fresh oranges at start → return 0
# 2. Fresh oranges exist but no rotten ones → return -1
# 3. Grid is all empty cells → return 0

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Step 1: Collect all initial rotten oranges, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If no fresh oranges from start
        if fresh == 0:
            return 0

        minutes_passed = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        # Step 2: Multi-source BFS
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If neighbor is a fresh orange, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes_passed += 1

        # Step 3: If fresh still remains, it's impossible
        return minutes_passed if fresh == 0 else -1


"""
# 🔄 Dry Run Example:
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]

Initial:
fresh = 6
queue = [(0,0)]

Minute 1:
- From (0,0) → rot (0,1) and (1,0)
fresh = 4
queue = [(0,1),(1,0)]

Minute 2:
- Rot neighbors of (0,1) and (1,0)
fresh = 2
queue = [(0,2),(1,1)]

Minute 3:
- Rot neighbors of (0,2) and (1,1)
fresh = 0
queue = [(2,1)]

End: minutes_passed = 4, fresh = 0 → return 4
"""