# LeetCode 173 - Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

# ✅ Problem:
# Implement an iterator over a binary search tree (BST). Your iterator should support the following operations:
#   - `next()`: returns the next smallest number
#   - `hasNext()`: returns whether there is a next smallest number

# 📚 Pattern:
# Stack-based Inorder Traversal Simulation
# Use a stack to simulate the recursion stack of an in-order traversal.

# 🧪 Subtype:
# Lazy Traversal using Controlled Stack
# Push only the necessary left path at each step.

# 🧠 Memory Hook:
# in-order traversal: Left → Node → Right
# use stack to hold left path
# after pop: move to right child, push left path again

# ✅ Time Complexity:
#   - `next()` and `hasNext()` average O(1) over n calls
# ✅ Space Complexity: O(h) where h is tree height (stack depth)

# 📌 Common Gotchas:
# - Forgetting to push left path when moving to right child
# - Not maintaining stack properly for in-order order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        # Stack for the controlled recursion
        self.stack = []
        # Initialize stack with the leftmost path of the root
        self._leftmost_inorder(root)

    # 🧭 Push all the way down to the leftmost node
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # 🔁 Return the next smallest number
    def next(self) -> int:
        # Pop the top node
        top = self.stack.pop()

        # After visiting this node, visit the right subtree
        if top.right:
            self._leftmost_inorder(top.right)

        return top.val

    # ✅ Check if there is a next smallest number
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# 🔍 Dry Run:
# Tree:
#      7
#     / \
#    3   15
#       /  \
#      9    20

# Initialization:
# stack = [7, 3] ← leftmost path from 7
#
# next() → pop 3 → return 3
# stack = [7]
#
# next() → pop 7 → return 7
# stack = []
# move to 15, push [15, 9]
#
# next() → pop 9 → return 9
#
# next() → pop 15 → return 15
# move to 20, push [20]
#
# next() → pop 20 → return 20

# Final result order: 3 → 7 → 9 → 15 → 20 ✅