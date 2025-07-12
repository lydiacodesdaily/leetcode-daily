# LeetCode 73 - Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

# ✅ Problem:
# Given an m x n integer matrix, if an element is 0,
# set its entire row and column to 0 in-place.

# 📚 Pattern:
# Matrix In-Place Marking with First Row & Column as Flags

# 🔍 Key Insight:
# - Instead of using extra space to mark which rows/cols to zero,
#   we use the first row and first column as marker arrays.
# - BUT we must handle the first row/column separately
#   to avoid overwriting our own markers early.

# 🧠 Memory Hook:
# "Use first row + col as flag boards"
# - matrix[0][j] == 0 → zero out col j
# - matrix[i][0] == 0 → zero out row i
# - Track separately: was_first_row_zero, was_first_col_zero

# ✅ Time Complexity: O(m * n)
# ✅ Space Complexity: O(1) — in-place

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Check if first row or first column has any zeros
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column as markers for the rest of the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to 0 based on the markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0


# 🔄 Dry Run:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
#
# Step 1 (mark):
# matrix[1][0] = 0
# matrix[0][1] = 0
#
# Step 2 (set to zero):
# matrix[1][1] = 0 (original)
# matrix[1][0] == 0 → zero entire row
# matrix[0][1] == 0 → zero entire col
#
# Final Output:
# [[1,0,1],
#  [0,0,0],
#  [1,0,1]]

# 🔸 Common Gotchas:
# - Forgetting to check/restore first row or column separately
# - Accidentally zeroing marker cells before reading them
#
# This is a classic **in-place optimization** technique. Make sure to explain clearly in interviews!
