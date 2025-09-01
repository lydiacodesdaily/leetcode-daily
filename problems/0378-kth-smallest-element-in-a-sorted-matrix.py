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
                    count += row + 1 # we are adding the #s above this row in this col 
                    col += 1  # Move right to next column, to see if we can also add #s above this row in the new col
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


#### VERSION 2 #####
# LeetCode 378 - Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
#
# ✅ Problem
# Given an n x n matrix where each row and column is sorted in ascending order,
# return the k-th smallest element.
#
# 📚 Pattern: Min-Heap (k-way merge by rows)
# - Treat each row as a sorted list.
# - Seed heap with the first element (col 0) from each of the first min(k, n) rows.
# - Pop the smallest; push its right neighbor from the same row; repeat k times.
#
# 🔍 Core Idea
# Keep a min-heap of triplets (value, r, c).
# Each pop gives the next smallest overall. If c+1 exists, push (matrix[r][c+1], r, c+1).
#
# 🧠 Memory Hook
# seed (r,0) for r in 0..min(k,n)-1
# repeat k: pop → push (r,c+1) if in-bounds
# heap size ≤ min(k,n)
#
# ✅ Time Complexity (why):
# - Heap build (heapify): O(min(k, n))   ← we initially insert up to min(k, n) items (first column of top rows).
# - Each of the k iterations does: one heappop (+ maybe one heappush).
#   Cost per op is O(log H) where H = heap size ≤ min(k, n).
#   So the loop is O(k log min(k, n)).
# ▶ Total: O(min(k, n) + k log min(k, n))
#
# ✅ Space Complexity (why):
# - Heap holds at most one candidate from each seeded row at any time → O(min(k, n)).
# - No visited set is required because we only move right within the same row (no duplicates inserted).
#
# 📌 Common Gotchas
# - Don’t seed all n rows if k < n. Use min(k, n) to keep the heap smaller.
# - Push only the right neighbor (r, c+1) after popping (r, c). Do NOT push downward neighbors here;
#   downward rows are already represented by their own seeds.
# - Remember to import heapq.
#
# 🔄 Tiny Dry Run
# matrix =
# [ 1,  5,  9]
# [10, 11, 13]
# [12, 13, 15], k=5
#
# seed: (1,0,0), (10,1,0), (12,2,0)
# pop1 → 1   push (5,0,1)
# pop2 → 5   push (9,0,2)
# pop3 → 9   (no push, end of row)
# pop4 → 10  push (11,1,1)
# pop5 → 11  ← answer
#
from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 0:
            return -1  # or raise, but LeetCode constraints guarantee n>=1

        # ----- 1) Seed heap with first element of each of the first min(k, n) rows -----
        # Triplet = (value, row_index, col_index)
        heap = []
        rows_to_seed = min(k, n)
        for r in range(rows_to_seed):
            heap.append((matrix[r][0], r, 0))
        heapq.heapify(heap)  # O(rows_to_seed)

        # ----- 2) Pop k times; each time, push right neighbor if exists -----
        # After the k-th pop, the popped 'val' is the k-th smallest overall.
        val = -1
        for _ in range(k):
            val, r, c = heapq.heappop(heap)  # O(log heap_size)
            if c + 1 < n:  # right neighbor exists
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))  # O(log heap_size)

        return val


# ----------------------------
# 🧪 Quick Embedded Example
# ----------------------------
if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(Solution().kthSmallest(matrix, 5))  # Expected: 11