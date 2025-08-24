# LeetCode 545 - Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/
#
# ✅ Problem:
# Return the boundary of a binary tree in anti-clockwise order starting from the root.
# Boundary = root + left boundary (exclude leaves) + all leaves (left→right) + reversed right boundary (exclude leaves).
#
# 📚 Pattern:
# Tree Traversal Decomposition (Left boundary → Leaves → Right boundary)
#
# 🔍 Core Idea:
# Decompose into 3 clean passes:
#   1) Left boundary: go as far left as possible (fallback to right), skip leaves.
#   2) Leaves: DFS collect all leaf nodes in left→right order.
#   3) Right boundary: go as far right as possible (fallback to left), skip leaves; collect then reverse.
#
# 🧠 Memory Hook:
# root once → left(no leaves) → leaves(all) → reverse(right no leaves)
# "Sides skip leaves, middle adds all leaves"
#
# ✅ Time Complexity: O(n) — each node processed O(1) across passes
# ✅ Space Complexity: O(h) recursion for leaves + O(h) buffer for right side (h = tree height)
#
# 📌 Common Gotchas:
# - Do NOT add leaves in left/right boundary helpers (avoid duplicates).
# - Reverse the right boundary at the end.
# - Single-node tree: answer is just [root].
# - Skewed trees: remember fallbacks (left-bound uses right when no left; right-bound uses left when no right).
#
# ————————————————————————————————————————————————————————————————

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # 0) Guard: empty tree
        if not root:
            return []

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        # If the root itself is a leaf, boundary is just [root]
        if is_leaf(root):
            return [root.val]

        boundary: List[int] = [root.val]  # root included exactly once

        # 1) Left boundary (iterative) — prefer left, fallback to right; skip leaves
        def add_left_boundary(node: Optional[TreeNode]) -> None:
            curr = node
            while curr:
                if not is_leaf(curr):
                    boundary.append(curr.val)
                # prefer left child, otherwise go right
                curr = curr.left if curr.left else curr.right

        # 2) Leaves (recursive DFS) — add all leaves left→right
        def add_leaves(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if is_leaf(node):
                boundary.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        # 3) Right boundary (iterative) — prefer right, fallback to left; skip leaves; push then reverse
        def add_right_boundary(node: Optional[TreeNode]) -> None:
            curr = node
            stack: List[int] = []
            while curr:
                if not is_leaf(curr):
                    stack.append(curr.val)
                # prefer right child, otherwise go left
                curr = curr.right if curr.right else curr.left
            # append in reverse order
            while stack:
                boundary.append(stack.pop())

        # Orchestrate passes
        add_left_boundary(root.left)
        add_leaves(root)
        add_right_boundary(root.right)

        return boundary

# ————————————————————————————————————————————————————————————————
# 🔄 Dry Run (visual example in comments):
#
# Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#       / \
#      8   9
#
# Steps:
# - root: [1]
# - left boundary (no leaves): go 2→(4 is leaf, stop before adding 4) → add [2]
# - leaves L→R: [4, 8, 9, 6, 7]
# - right boundary (no leaves, reversed): 3→(7 is leaf, stop) → collect [3] → reverse → [3]
# Result: [1, 2, 4, 8, 9, 6, 7, 3]
#
# ————————————————————————————————————————————————————————————————
# 🧪 Quick Self-Test:

def _build_example():
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(5); n6 = TreeNode(6); n7 = TreeNode(7)
    n8 = TreeNode(8); n9 = TreeNode(9)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n5.left, n5.right = n8, n9
    n3.left, n3.right = n6, n7
    return n1

if __name__ == "__main__":
    root = _build_example()
    print(Solution().boundaryOfBinaryTree(root))  # [1, 2, 4, 8, 9, 6, 7, 3]