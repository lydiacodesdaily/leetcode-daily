# LeetCode 510 - Inorder Successor in BST II
# https://leetcode.com/problems/inorder-successor-in-bst-ii/

# ✅ Problem:
# Given a node `p` in a Binary Search Tree (where each node has a parent pointer),
# return its inorder successor node (node with smallest value greater than p.val).
# Return None if no successor exists.

# 📚 Pattern:
# Inorder Successor with Parent Pointer

# 🔍 Key Insight:
# - If p has right child → successor = leftmost of p.right
# - Else → walk UP via p.parent until you find a node where you came from the left

# 🧠 Memory Hook:
# → right child? go down to leftmost
# → no right? go up until from left

# ✅ Time Complexity: O(h), where h = height of tree
# ✅ Space Complexity: O(1)

class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 🧩 Case 1: If right child exists → successor is leftmost of right subtree
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        # 🧩 Case 2: No right child → walk up via parent until you come from the left
        curr = node
        while curr.parent and curr == curr.parent.right:
            curr = curr.parent
        
        """
        # 285 - find the candidate from the root 
        successor = None 
        while root:
            if p.val < root.val:
                successor = root.val 
                root = root.left
            else: # p.val >= root.val
                root = root.right
        """
        
        return curr.parent  # May be None (no successor)

# 🔄 Dry Run Example:
#
#        6
#       / \
#      3   8
#     / \    
#    2   4
#         \
#          5
#
# p = 5 → successor = 6
#
# Step-by-step:
# - No right child
# - Climb up: 5 → 4 → 3 → 6
# - 3 was left child of 6 → return 6 ✅