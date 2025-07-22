# LeetCode 529 - Minesweeper
# https://leetcode.com/problems/minesweeper/

# ✅ Problem:
# Given a Minesweeper board and a user click, reveal the board state according to the game's rules:
# - Clicked 'M' → turn to 'X'
# - Clicked 'E' with adjacent mines → turn to '1'–'8'
# - Clicked 'E' with no adjacent mines → turn to 'B' and recursively reveal neighbors

# 📚 Pattern:
# DFS / Flood-Fill Simulation on Grid

# 🔍 Key Insight:
# - Use DFS to reveal cells
# - Stop recursion if:
#   - Cell is not 'E'
#   - Cell has adjacent mines (convert to number, do not expand)
# - Recurse only when cell is 'E' **and** has 0 adjacent mines

# 🧠 Memory Hook (BDBS):
# B = Bounds check: stay within grid
# D = Directions: 8 neighbors
# B = Base case: stop if not 'E'
# S = State update: mark as 'B', number, or 'X'

# ✅ Time Complexity: O(m * n) in worst case (reveal all cells)
# ✅ Space Complexity: O(m * n) stack space (worst-case recursion depth)

# 📌 Common Gotchas:
# - Don't reveal further if cell has adjacent mines
# - Use in-place marking to avoid visited set
# - Must handle all 8 directions (including diagonals)

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])
        r0, c0 = click

        # ✅ D = Directions (8-directional flood fill)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Helper to count adjacent mines
        def count_mines(r, c):
            # ✅ B + D: Bounds check + neighbor iteration
            return sum(
                0 <= r+dr < ROWS and 0 <= c+dc < COLS and board[r+dr][c+dc] == 'M'
                for dr, dc in directions
            )

        # DFS function to reveal cells
        def dfs(r, c):
            # ✅ B + B: Bounds + Base case
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != 'E':
                return

            # Count adjacent mines first
            mines = count_mines(r, c)

            if mines > 0:
                # ✅ S = State update: show number and stop
                board[r][c] = str(mines)
            else:
                # ✅ S = State update: no mines → 'B'
                board[r][c] = 'B'
                # ✅ D = Expand to all 8 neighbors recursively
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        # ✅ Entry point logic
        if board[r0][c0] == 'M':
            # ✅ S = State update: click a mine → boom
            board[r0][c0] = 'X'
        else:
            dfs(r0, c0)

        return board

# 🔄 Dry Run Example:
# Input board:
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
#
# Click: [3, 0]
# → Board will flood-fill empty 'E's until a numbered cell (adjacent to mine) is found
# → Final revealed board will reflect correct cascade