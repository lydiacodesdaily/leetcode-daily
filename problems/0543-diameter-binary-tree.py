# LeetCode 543 - Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# ✅ Problem:
# Given a binary tree, return the length of the diameter (longest path between any two nodes).
# The path may or may not pass through the root. Return the **number of edges**, not nodes.

# 📚 Pattern:
# DFS (Postorder) — Track diameter during height computation

# 🔍 Core Idea:
# For each node, the longest path through it = left height + right height.
# So while computing height, track the maximum diameter seen so far.
# diameter = maximum number of edges between two nodes in the tree
# therefore, no need to add "1" to left + right

# 🧠 Memory Hook:
# postorder DFS
# update diameter = max(left + right) 
# return height = 1 + max(left, right)

# ✅ Time Complexity: O(n) — visit every node once
# ✅ Space Complexity: O(h) — recursive call stack (h = height)

# 📌 Common Gotchas:
# - Diameter counts **edges**, so don’t +1 when returning
# - Must update global diameter inside DFS

from typing import Optional

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
