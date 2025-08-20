# LeetCode 498 - Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/

# ✅ Problem:
# Given an m x n matrix, return all elements of the matrix in diagonal order.

# 🔍 Key Insight:
# Diagonals in a matrix follow a pattern:
# - Each diagonal has the same sum of indices: i + j
# - We alternate the direction of traversal for each diagonal (up ↔ down)
# elements on the same diagonal share the same sum of indices: i + j.
# In a matrix of size m x n:
# - The smallest diagonal key is 0 → from matrix[0][0]
# - The largest diagonal key is (m - 1) + (n - 1) → from matrix[m - 1][n - 1]
# - So total diagonals: (m - 1) + (n - 1) + 1 = m + n - 1

# 📚 Pattern: Matrix Traversal with Diagonal Grouping

# 🧪 Subtype: Group by i + j (diagonal level)
# - Use a dictionary: diagonals[sum] = list of elements
# - For even-indexed diagonals (i+j), reverse before adding to result

# 🧠 Memory Hook:
# diagonal = i + j
# use dict to group all cells by diagonal
# even → reverse, odd → keep order

# ✅ Time Complexity: O(m * n) — visit each element once
# ✅ Space Complexity: O(m * n) — output + map of diagonals

# 📌 Common Gotchas:
# - Be careful with alternating direction of diagonals
# - Reversing only even diagonals gives desired zigzag pattern

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = collections.defaultdict(list)

        # 🧭 Step 1: Group elements by the sum of indices (i + j)
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        result = []

        # 🧭 Step 2: Traverse diagonals in order of their key (0 → m+n-2)
        for k in range(m + n - 1):
            if k % 2 == 0:
                # even diagonals → reverse
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])

        return result

# 🔄 Dry Run:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Diagonals:
# sum=0 → [1]
# sum=1 → [2,4]
# sum=2 → [3,5,7]
# sum=3 → [6,8]
# sum=4 → [9]
# Direction:
# sum=0 (even) → [1]
# sum=1 (odd) → [2,4]
# sum=2 (even) → [7,5,3]
# sum=3 (odd) → [6,8]
# sum=4 (even) → [9]
# Result: [1,2,4,7,5,3,6,8,9] ✅