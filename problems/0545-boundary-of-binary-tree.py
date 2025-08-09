# LeetCode 545 - Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/
#
# ✅ Problem:
# Return the boundary of a binary tree in counter-clockwise order starting from the root.
# Boundary = root + left boundary (excluding leaves) + leaves (left→right) + right boundary (excluding leaves, reversed).
#
# 📚 Pattern:
# Binary Tree Traversal by zones (left-boundary, leaves, right-boundary)
#
# 🔍 Core Idea:
# Decompose into 3 clean passes to avoid duplicates:
#   1) Walk down the left edge, adding non-leaf nodes.
#   2) DFS all leaves (left→right).
#   3) Walk down the right edge, collecting non-leaf nodes, then reverse and append.
#
# 🧠 Memory Hook:
# "root → left-edge → leaves → right-edge(rev)"
# - skip leaves in edges
# - collect right edge, then reverse
# - single-node tree → just [root]
#
# ✅ Time Complexity: O(n) — every node visited O(1) times
# ✅ Space Complexity: O(h) recursion for leaves DFS (+ O(h) temp for right edge)
#
# 📌 Common Gotchas:
# - Don’t duplicate leaves that also lie on edges.
# - Exclude leaves from left/right boundaries.
# - For skewed trees (only left or only right), logic should still work.
# - Empty tree → [].
#
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # --------
        # Guard: empty
        # --------
        if not root:
            return []

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        boundary = []

        # --------
        # 0) Root
        # --------
        if not is_leaf(root):
            boundary.append(root.val)
        else:
            # single-node tree → boundary is just [root]
            return [root.val]

        # --------
        # 1) Left boundary (exclude leaves)
        #    Walk down preferring .left then .right when .left missing.
        # --------
        cur = root.left
        while cur:
            if not is_leaf(cur):
                boundary.append(cur.val)
            # prefer going left; if not available, go right to stay on "edge"
            cur = cur.left if cur.left else cur.right

        # --------
        # 2) Leaves (in-order DFS left→right)
        #    Collect all leaves; this includes those not on edges.
        # --------
        def add_leaves(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if is_leaf(node):
                boundary.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root)

        # --------
        # 3) Right boundary (exclude leaves) — collect and reverse
        #    Walk down preferring .right then .left when .right missing.
        # --------
        stack = []
        cur = root.right
        while cur:
            if not is_leaf(cur):
                stack.append(cur.val)
            cur = cur.right if cur.right else cur.left

        # append in reverse to keep counter-clockwise order
        while stack:
            boundary.append(stack.pop())

        return boundary


# 🧩 Embedded Example:
# Tree:
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6
#     / \  / \
#    7  8 9  10
#
# Expected boundary (CCW):
# root: 1
# left-edge (no leaves): 2, 4 is a leaf → exclude here
# leaves L→R: 4,7,8,9,10
# right-edge (no leaves) reversed: 3,6  (since walk was 6,3 → reverse)
# => [1, 2, 4, 7, 8, 9, 10, 6, 3]

# 🔄 Dry Run (sketch):
# boundary = [1]
# left-edge: visit 2 (non-leaf) → boundary=[1,2]; then go to 4 (leaf) → skip here.
# leaves DFS adds: [4,7,8,9,10]
# right-edge collect stack=[6,3] (exclude leaves), then reverse & extend → [3,6]
# final = [1,2,4,7,8,9,10,6,3]