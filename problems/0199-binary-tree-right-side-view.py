# LeetCode 199 - Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# ✅ Problem:
# Given a binary tree, return the values of the nodes you can see from the right side,
# ordered from top to bottom.

# 📚 Pattern:
# BFS - Level Order Traversal

# 🔍 Core Idea:
# Traverse the tree level by level using a queue.
# At each level, add the **last node’s value** (rightmost) to the result list.

# 🧠 Memory Hook:
# - level order traversal
# - last node in level = rightmost visible
# - append `level[-1].val` to result

# ✅ Time Complexity: O(n) — visit each node once
# ✅ Space Complexity: O(n) — queue space for level traversal

# 📌 Common Gotchas:
# - Don’t confuse “right child” with “right side view”
# - Use `for _ in range(len(queue))` to isolate each level cleanly

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        # 🌱 BFS traversal
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # 👀 Capture the last node of the current level
                if i == level_size - 1:
                    result.append(node.val)

                # 🌿 Push left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# 🔄 Dry Run:
# Tree:
#       1
#     /   \
#    2     3
#     \     \
#      5     4

# Levels:
# [1] → add 1
# [2,3] → add 3
# [5,4] → add 4

# Output: [1, 3, 4]