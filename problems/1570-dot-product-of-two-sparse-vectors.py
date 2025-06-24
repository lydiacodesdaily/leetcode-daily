# LeetCode 1570 - Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

# ✅ Problem:
# Given two sparse vectors, compute their dot product efficiently.

# 🧩 Base Pattern:
# Hash Map Intersection
# - Only store non-zero entries to reduce space
# - Only multiply when both vectors have a value at the same index

# 🧪 Subtype:
# Dictionary Intersection with Multiplication
# - Store index:value for non-zero entries
# - Traverse the smaller dict and check for overlap in the other

# 🔍 Key Insight:
# sparse vector = most elements are 0s
# instead of storing full arrs, we store: v1_sparse = {2: 3, 4: 4}  # index → value
# dotproduct:  only multiply values where both vectors are non-zero at the same index → much faster and space-efficient.
# v1[2] * v2[2] + v1[4] * v2[4] = 3*0 + 4*5 = 0 + 20 = 20

# 🧠 Memory Hook:
# sparse vec → dict of index:val
# dot = sum(v1[i] * v2[i]) only when i in both
# iterate over smaller dict for speed

# ✅ Time Complexity: O(L1 + L2) for preprocessing, then O(min(L1, L2)) for dot product
# ✅ Space Complexity: O(L1 + L2) for storing both sparse maps

class SparseVector:
    def __init__(self, nums: list[int]):
        # Store only non-zero elements with their indices
        self.sparse = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Iterate over the smaller sparse vector for better performance
        if len(self.sparse) > len(vec.sparse):
            return vec.dotProduct(self)

        total = 0
        for i in self.sparse:
            if i in vec.sparse:
                total += self.sparse[i] * vec.sparse[i]
        return total

# 🔄 Dry Run:
# vec1 = [0, 1, 0, 0, 2, 0, 0]
# vec2 = [0, 0, 3, 0, 4, 0, 0]
#
# Sparse 1: {1: 1, 4: 2}
# Sparse 2: {2: 3, 4: 4}
#
# Only common index = 4 → 2 * 4 = 8
# return 8 ✅

# 📌 Common Gotchas:
# - Only compare when index exists in both vectors
# - Be sure to optimize by looping over the smaller dict
# - Don’t forget to handle 0-length or fully zero vectors gracefully