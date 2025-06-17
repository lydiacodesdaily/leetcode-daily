# LeetCode 938 - Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# ✅ Problem:
# Given the root of a Binary Search Tree (BST) and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# 🔍 Key Insight:
# Because this is a BST, we can **prune** unnecessary branches to avoid unnecessary recursion:
# - If node.val < low, then left subtree is too small → only explore the right
# - If node.val > high, then right subtree is too large → only explore the left
# - If node.val is within [low, high], include it and explore both subtrees

# ✅ Time Complexity: O(n) worst case (unbalanced tree); O(log n) best case with pruning
# ✅ Space Complexity: O(h) where h = height of the tree (recursion stack)

# 📚 Pattern: Binary Search Tree + DFS + Pruning

# 🔁 Dry Run:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Tree:
#         10
#        /  \
#       5    15
#      / \     \
#     3   7     18
#
# Step-by-step:
# - 10 is in range → sum = 10
#   - Left: 5 < 7 → skip 3, check right (7)
#     - 7 in range → sum += 7
#   - Right: 15 in range → sum += 15
#     - 18 > 15 → skip
# Total = 10 + 7 + 15 = 32

# 📌 Common Gotchas:
# - Don't forget [low, high] is inclusive
# - If you treat the tree like a normal binary tree without pruning, you'll lose efficiency

# 🧠 Concept Reinforced:
# - Use BST properties to reduce unnecessary recursion
# - Condition-based DFS pruning

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            # current value too small → skip left subtree
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            # current value too large → skip right subtree
            return self.rangeSumBST(root.left, low, high)
        else:
            # current node is in range → include its value
            return (
                root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high)
            )