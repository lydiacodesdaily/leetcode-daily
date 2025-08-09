# LeetCode 419 - Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/
#
# ✅ Problem:
# Count the number of battleships on a 2D board. Ships are placed either
# horizontally or vertically, never adjacent (no two ships touch except by
# being part of the same continuous ship segment). Cells are 'X' (ship) or '.'.
#
# 📚 Pattern:
# Matrix scan with "start-of-segment" detection
#
# 🔍 Core Idea:
# A NEW ship begins at cell (i, j) if board[i][j] == 'X' and there is no 'X'
# directly above it and no 'X' directly to its left. Each ship contributes
# exactly one such "top-left" cell—count those.
#
# 🧠 Memory Hook:
# "count top-left X’s only"
# - if board[i][j] == 'X'
# - and board[i-1][j] != 'X' (no top)
# - and board[i][j-1] != 'X' (no left)
# → count++
#
# ✅ Time Complexity: O(m * n)
# ✅ Space Complexity: O(1)
#
# 📌 Common Gotchas:
# - Don't count every 'X'—only the first cell in a ship (no top, no left).
# - Avoid modifying the board or using extra memory.
# - Check bounds before looking up top/left neighbors.

from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # --------
        # Guard: empty board
        # --------
        if not board or not board[0]:
            return 0

        m, n = len(board), len(board[0])
        ships = 0

        # --------
        # Single pass: count "top-left starts"
        # --------
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    continue

                # Check if there's an 'X' above
                has_top = (i > 0 and board[i - 1][j] == 'X')
                # Check if there's an 'X' to the left
                has_left = (j > 0 and board[i][j - 1] == 'X')

                # Count only when current 'X' is the first cell of a battleship
                if not has_top and not has_left:
                    ships += 1

        return ships


# 🔄 Dry Run:
# Input:
# board = [
#   ["X",".",".","X"],
#   [".",".",".","X"],
#   [".",".",".","X"]
# ]
#
# Walkthrough:
# (0,0)='X': no top, no left → ships=1
# (0,1)='.' skip
# (0,2)='.' skip
# (0,3)='X': no top, no left → ships=2  (this is the top of the vertical ship)
# (1,0)='.' skip
# (1,3)='X': has_top (0,3)='X' → not a new ship
# (2,3)='X': has_top (1,3)='X' → not a new ship
#
# Result: 2 ✅

# 🧩 Example:
# board = [
#   ["X",".",".","X"],
#   [".",".",".","X"],
#   [".",".",".","X"]
# ]
# Solution().countBattleships(board) -> 2