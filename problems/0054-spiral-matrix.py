# LeetCode 54 - Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
#
# ✅ Problem:
# Given an m x n matrix, return all elements in spiral order (clockwise).
#
# 📚 Pattern:
# Matrix layer-by-layer traversal (simulation with shrinking boundaries)
#
# 🔍 Core Idea:
# Use four boundaries to represent the current layer:
#   top, bottom, left, right
# Traverse in 4 steps:
#   1) left → right on 'top' row;   then top += 1
#   2) top → bottom on 'right' col; then right -= 1
#   3) right → left on 'bottom' row; then bottom -= 1   (only if top <= bottom)
#   4) bottom → top on 'left' col;   then left += 1     (only if left <= right)
# Repeat while top <= bottom and left <= right.
#
# 🧠 Memory Hook:
# bounds: top,bottom,left,right
# traverse 4 edges → shrink corresponding bound
# guard steps 3 & 4 with checks to avoid duplicates
#
# ✅ Time Complexity: O(m * n)   (visit each cell once)
# ✅ Space Complexity: O(1) extra (output list not counted)
#
# 📌 Common Gotchas:
# - Forgetting to check conditions before steps 3 & 4 (single row/col layers → duplicates).
# - Wrong order of shrinking bounds (shrink after finishing each edge).
# - Off-by-one in while condition (must be while top <= bottom and left <= right).
#
# 🔄 Dry Run (quick):
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# top=0,bottom=2,left=0,right=2
# 1) top row: 1,2,3; top=1
# 2) right col: 6,9; right=1
# 3) bottom row (check top<=bottom): 8,7; bottom=1
# 4) left col   (check left<=right): 4;   left=1
# Loop again:
# 1) top row: 5; top=2
# Now top(2) > bottom(1) → stop. Result = [1,2,3,6,9,8,7,4,5]
#
# --- Clean interview implementation (grouped skeletal steps) ---

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # 🧭 Traverse while the current layer is valid
        while top <= bottom and left <= right:
            # 1) left → right on top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2) top → bottom on right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3) right → left on bottom row (only if still within bounds)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4) bottom → top on left column (only if still within bounds)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res


# --- Embedded Examples ---
# Example 1:
# Input:  [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input:  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]