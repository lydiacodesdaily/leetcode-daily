# LeetCode 766 - Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

# ✅ Problem:
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Return True if the matrix is Toeplitz. Otherwise, return False.

# 📚 Pattern: Matrix Traversal

# 🔍 Key Insight:
# Each cell (i, j) should equal matrix[i-1][j-1] if i > 0 and j > 0

# 🧠 Memory Hook:
# for i, j > 0 → matrix[i][j] == matrix[i-1][j-1]
# check all cells except first row/column

# ✅ Time: O(m * n) — visit every cell once
# ✅ Space: O(1) — no extra space used

# 📌 Common Gotchas:
# - Accidentally check first row/col and go out of bounds
# - Forget that diagonals move → down-right, so compare with up-left

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # 🧭 Compare each cell to the top-left diagonal element
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True

# 🔄 Dry Run:
# Input: matrix = [[1,2,3],[4,1,2],[5,4,1]]
# Valid because:
# - (1,1)=1 == (0,0)=1
# - (1,2)=2 == (0,1)=2
# - (2,1)=4 == (1,0)=4
# - (2,2)=1 == (1,1)=1 ✅