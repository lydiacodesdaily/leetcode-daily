# LeetCode 426 - Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# ✅ Problem:
# Given the root of a Binary Search Tree (BST), convert it to a 
# sorted circular doubly-linked list **in-place**.
#
# - Each node has: val, left, and right
# - The "left" pointer will act as "prev"
# - The "right" pointer will act as "next"
# - Return the head of the circular DLL

# 📚 Pattern:
# In-order traversal (DFS) — since it naturally visits nodes in sorted order

# 🔍 Key Insight:
# - Traverse the tree in-order (Left → Node → Right)
# - While visiting, link:
#     last.right = current
#     current.left = last
# - After traversal, connect head ↔ tail to make it circular

# 🧠 Memory Hook:
# in-order traversal gives sorted order
# connect (last ↔ curr) as you go
# at end, connect (head.left = tail) and (tail.right = head)

# ✅ Time Complexity: O(n) — visit every node once
# ✅ Space Complexity: O(h) — recursion stack (h = height of tree)

class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Pointers to track the head (smallest) and tail (last visited) nodes
        self.first = None
        self.last = None

        # 🧭 In-order DFS traversal
        def dfs(node):
            if not node:
                return

            # Traverse left subtree
            dfs(node.left)

            # 🔗 Connect last ↔ node
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node  # First (smallest) node becomes head of DLL

            self.last = node  # Move last pointer forward

            # Traverse right subtree
            dfs(node.right)

        dfs(root)

        # 🔁 Connect head and tail to form circular DLL
        self.first.left = self.last
        self.last.right = self.first

        return self.first

# 🔄 Dry Run Example:
# Input: BST
#       4
#     /   \
#    2     5
#   / \
#  1   3
#
# In-order: 1 → 2 → 3 → 4 → 5
# Output DLL: 1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5 (circular)
# - 1.left = 5, 5.right = 1

# -------------------------------
# 🔄 DRY RUN (write these as comments while coding)
# Tree:
#        4
#      /   \
#     2     5
#    / \
#   1   3
#
# Inorder: 1, 2, 3, 4, 5  (this will be the DLL order)
#
# Init:
#   first=None, last=None
#
# dfs(4)
#   dfs(2)
#     dfs(1)
#       dfs(None) -> return
#       visit(1):
#         last is None → first=1
#         last=1
#       dfs(None) -> return
#     visit(2):
#       last=1 → link 1<->2:
#         1.right=2
#         2.left=1
#       last=2
#     dfs(3)
#       dfs(None) -> return
#       visit(3):
#         last=2 → link 2<->3:
#           2.right=3
#           3.left=2
#         last=3
#       dfs(None) -> return
#   visit(4):
#     last=3 → link 3<->4:
#       3.right=4
#       4.left=3
#     last=4
#   dfs(5)
#     dfs(None) -> return
#     visit(5):
#       last=4 → link 4<->5:
#         4.right=5
#         5.left=4
#       last=5
#     dfs(None) -> return
#
# After DFS:
#   first=1, last=5
#   Close circle:
#     first.left = last  → 1.left = 5
#     last.right = first → 5.right = 1
#
# DLL (circular):
#   1 <-> 2 <-> 3 <-> 4 <-> 5
#   and 5.right -> 1, 1.left -> 5