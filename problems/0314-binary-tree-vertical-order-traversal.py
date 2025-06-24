# LeetCode 314 - Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# ✅ Problem:
# Given a binary tree, return the vertical order traversal of its nodes' values.
# Traverse column by column from left to right, and within each column, top to bottom.
# If nodes share the same row and column, order them from left to right.

# 🔍 Key Insight:
# Do a **BFS traversal** while tracking column index:
# - Use a queue: (node, column)
# - Use a dictionary: col → list of values
# Track `min_col` and `max_col` to extract ordered result.

# 🧠 Memory Hook:
# use BFS with (node, column) → preserve top-down order  
# track min_col, max_col → to build result from left to right  
# use hashmap[col] → list of values in that vertical  
# final result: [hashmap[c] for c in range(min_col, max_col + 1)]

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)
# n = number of nodes

from collections import defaultdict, deque
from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # column index → list of node values
        col_table = defaultdict(list)
        # BFS queue with (node, column_index)
        queue = deque([(root, 0)])
        
        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            col_table[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [col_table[i] for i in range(min_col, max_col + 1)]