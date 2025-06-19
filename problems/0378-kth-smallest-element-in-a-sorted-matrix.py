# LeetCode 378 - Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# ✅ Problem:
# Find the kth smallest number in an n x n matrix sorted in both rows and columns.

# 🧩 Base Pattern:
# Binary Search on Value Space

# 🧪 Subtype:
# Counting how many elements are ≤ mid using smart traversal

# 📚 Pattern: Binary Search + Sorted Matrix

# 🧠 Memory Hook:
# binary search: on value range (min to max)
# count elements ≤ mid → move left or right
# matrix[row][col] ≤ mid → all above also valid → count += row + 1, col += 1
# return left (first value with at least k elements ≤ it)

# ✅ Time Complexity: O(n * log(max - min))
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Trying to binary search indices (instead of values)
# - Not starting from bottom-left corner when counting
# - Returning mid instead of left

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        # Helper to count elements ≤ target in the matrix
        def countLessEqual(mid: int) -> int:
            row, col = n - 1, 0  # Start from bottom-left
            count = 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # All values in current column above this row are also ≤ mid
                    count += row + 1
                    col += 1  # Move right to next column
                else:
                    # Value too big, move up
                    row -= 1
            return count

        # Binary search over the value range
        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1  # Not enough elements ≤ mid → try higher
            else:
                right = mid     # Enough elements ≤ mid → try smaller

        return left  # Smallest value with ≥ k elements ≤ it