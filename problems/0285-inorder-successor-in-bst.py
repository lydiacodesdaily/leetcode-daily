# LeetCode 285 - Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/

# ✅ Problem:
# Given the root of a Binary Search Tree and a node `p`,
# return the inorder successor of `p` in the BST.
# The successor is the node with the smallest key strictly greater than `p.val`.

# 📚 Pattern:
# BST Traversal + Inorder Successor Logic (2 Cases)

# 🔍 Key Insight:
# Case 1: If p.right exists → return leftmost node in right subtree
# Case 2: Otherwise → walk down from root, track first node > p

# 🧠 Memory Hook:
# → if right exists → leftmost in right
# → else walk from root, update candidate if node > p

# ✅ Time Complexity: O(h), where h = height of tree
# ✅ Space Complexity: O(1)

from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Case 1: If right child exists → successor is leftmost in right subtree
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr

        # Case 2: No right child → traverse from root and track candidate
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right  # ✅ FIXED: was root.left in buggy version

        return successor


# 🔍 Edge Case Checklist (with example inputs for reference):

"""
Edge Case 1: No successor exists (p is the largest node)
Tree: [20, 10, 30], p = 30 → Expected: None

Edge Case 2: p has a right subtree
Tree: [20, 10, 30, None, None, 25, 35], p = 20 → Expected: 25

Edge Case 3: p has no right subtree; successor is one of its ancestors
Tree: [20, 10, 5, 15, 30], p = 15 → Expected: 20

Edge Case 4: Tree with only one node
Tree: [42], p = 42 → Expected: None

Edge Case 5: p is the root, has right child
Tree: [10, 5, 15, None, None, 12, 20], p = 10 → Expected: 12

Edge Case 6: p is a left leaf node
Tree: [10, 5, 15], p = 5 → Expected: 10

Edge Case 7: p is a right leaf node with no successor
Tree: [10, 5, 15], p = 15 → Expected: None

Edge Case 8: p is not in the tree (invalid input)
→ Behavior is undefined unless assumption is made that `p` is in the tree
"""