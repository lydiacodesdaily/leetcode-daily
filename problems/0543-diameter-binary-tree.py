from typing import Optional

# LeetCode 543: Diameter of Binary Tree
# ✨ Problem:
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter is the number of **edges** on the longest path between any two nodes in the tree.
#
# ⏱ Time Complexity: O(n), where n is the number of nodes
# 🔢 Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Step 1: Get the height of left and right subtree
            left = dfs(node.left)
            right = dfs(node.right)

            # Step 2: Update max_diameter if path through current node is longer
            self.max_diameter = max(self.max_diameter, left + right)

            # Step 3: Return height of the current subtree
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter

# ✅ Dry Run Example:
# Input: [1, 2, 3, 4, 5]
# Tree Structure:
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# Longest path: 4 -> 2 -> 5 => 2 edges left + 2 edges right = 3 total edges
# Output: 3
