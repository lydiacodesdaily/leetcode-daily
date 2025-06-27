# LeetCode 226 - Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# ✅ Problem:
# Invert a binary tree (mirror it) by swapping the left and right child of all nodes.

# 📚 Pattern:
# Recursive Depth-First Search (DFS) - Postorder traversal

# 🔍 Core Idea:
# At each node:
# - Swap left and right children
# - Recursively invert left and right subtrees

# 🧠 Memory Hook:
# swap left ↔ right
# postorder: invert left, invert right, then swap
# return root to rebuild tree structure

# ✅ Time Complexity: O(n) → visit each node once
# ✅ Space Complexity: O(h) → recursion stack (h = tree height)

# 📌 Common Gotchas:
# - Forgetting to return the root at each recursive step
# - Misunderstanding traversal order → swap should happen **after** children are inverted (postorder is cleanest)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 🔝 Base case: if tree is empty
        if not root:
            return None

        # 🔀 Recursive step:
        # Invert left subtree
        left_inverted = self.invertTree(root.left)

        # Invert right subtree
        right_inverted = self.invertTree(root.right)

        # 🔄 Swap left and right children
        root.left = right_inverted
        root.right = left_inverted

        # ✅ Return current root to rebuild the inverted tree
        return root


# 🔄 Dry Run:
# Input Tree:
#     4
#    / \
#   2   7
#
# Step 1:
# - Invert left subtree (node 2)
# - Invert right subtree (node 7)
# - Swap → left = 7, right = 2
#
# Step 2 (node 2):
# - Invert left = None → returns None
# - Invert right = None → returns None
# - Swap → still None, returns node 2
#
# Step 3 (node 7):
# - Invert left = None → returns None
# - Invert right = None → returns None
# - Swap → still None, returns node 7
#
# Final Tree:
#     4
#    / \
#   7   2
