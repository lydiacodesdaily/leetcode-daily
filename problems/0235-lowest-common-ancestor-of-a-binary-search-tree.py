# LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# ✅ Problem:
# Given a BST, and two nodes p and q,
# return their **lowest common ancestor (LCA)** —
# the lowest node in the tree that has both p and q as descendants.

# 📚 Pattern:
# Binary Search Tree Property Traversal

# 🔍 Key Insight:
# Use the BST property to navigate:
# - If p.val < root.val and q.val < root.val → LCA is in left subtree
# - If p.val > root.val and q.val > root.val → LCA is in right subtree
# - Else (split case) → current node is the LCA

# 🧠 Memory Hook:
# "Both left → go left"
# "Both right → go right"
# "Split → this is the LCA"

# ✅ Time Complexity: O(h) → h = height of the tree
# ✅ Space Complexity: O(1) if iterative, O(h) if recursive (call stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # 🧭 Traverse the tree using BST property
        while root:
            # 🡒 Both nodes in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # 🡒 Both nodes in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                # 🟢 Split case or one is equal to root → found LCA
                return root
"""
🔄 Dry Run:
Tree:       6
          /   \
         2     8
        / \   / \
       0   4 7   9
          / \
         3   5

p = 2, q = 8
→ 2 < 6 and 8 > 6 → split → return 6 ✅

p = 2, q = 4
→ both < 6 → go left
→ root = 2 → 2 == p → return 2 ✅
"""