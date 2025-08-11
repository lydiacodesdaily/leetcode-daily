# LeetCode 74 - Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
#
# ✅ Problem:
# Given an m x n matrix where:
#   1) Each row is sorted left→right
#   2) The first element of each row > last element of the previous row
# Determine if target is in the matrix. Return True/False.
#
# 📚 Pattern:
# Binary Search on a "flattened" 2D array (treat as 1D of length m*n)
#
# 🔍 Key Insight:
# Because row starts are strictly greater than previous row ends,
# the entire matrix is globally sorted if flattened. So we can binary search
# on index range [0 .. m*n - 1] and map mid → (row, col) using:
#   row = mid // n
#   col = mid % n
#
# 🧠 Memory Hook:
# "Flatten to 1D"
# row = mid // n
# col = mid % n
# compare matrix[row][col] with target
#
# ✅ Time Complexity: O(log(m*n))  (binary search over all elements)
# ✅ Space Complexity: O(1)
#
# 📌 Common Gotchas:
# - Mixing this up with LC 240 (that one uses top-right sweep; THIS one uses 1D binary search).
# - Wrong mid→(row, col) mapping (use n = number of columns).
# - Empty matrix or empty first row → return False early.
#
# 🔄 Dry Run (quick):
# matrix = [
#   [1,  3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 60]
# ], target = 16
# m=3, n=4 → search 0..11
# left=0, right=11
# mid=5 → (5//4=1, 5%4=1) → matrix[1][1]=11 < 16 → left=6
# mid=8 → (8//4=2, 8%4=0) → matrix[2][0]=23 > 16 → right=7
# mid=6 → (6//4=1, 6%4=2) → matrix[1][2]=16 == target → True ✅
#
# --- Clean interview implementation (grouped skeletal steps) ---

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # --- 0) Guard: empty matrix or empty row ---
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # --- 1) Binary search on the flattened index space [0 .. m*n-1] ---
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # --- 2) Map 1D 'mid' to 2D (row, col) ---
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            # --- 3) Standard binary search compare/shift ---
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        # --- 4) Not found ---
        return False


# --- Embedded Examples ---
# Example 1:
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 → True
#
# Example 2:
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 → False