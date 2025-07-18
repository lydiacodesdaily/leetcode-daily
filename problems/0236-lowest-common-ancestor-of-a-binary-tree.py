# LeetCode 236 - Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# ✅ Problem:
# Given a binary tree, find the **lowest common ancestor (LCA)** of two given nodes `p` and `q`.
# The LCA is the lowest node in the tree that has both `p` and `q` as descendants.

# 🔍 Key Insight:
# Use **postorder DFS traversal**:
# - If current node is None → return None
# - If current node is p or q → return node
# - Recursively search left and right
# - If both sides return non-null → current node is the LCA
# - If only one side returns non-null → propagate that up

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(h) — recursion stack; h = height of the tree

from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # Found p in one side, q in the other

        return left if left else right

# 🔁 Dry Run Example:
# Tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#
# Input: p = 7, q = 4
# Goal: Find LCA of 7 and 4 → Expected: 2

# Call Stack Trace:
# LCA(3)
# ├── LCA(5)
# │   ├── LCA(6) → None
# │   └── LCA(2)
# │       ├── LCA(7) → 7 (matches p)
# │       └── LCA(4) → 4 (matches q)
# │       → left = 7, right = 4 → return 2 ✅
# │   → return 2
# └── LCA(1) → no match → returns None
# → LCA(3): left = 2, right = None → return 2 ✅

# Final Result: 2

# ✅ Return Rules Summary:
# - If root is None → return None
# - If root == p or q → return root
# - If both left and right are non-null → return current root (this is the LCA)
# - If only one is non-null → propagate that one upward