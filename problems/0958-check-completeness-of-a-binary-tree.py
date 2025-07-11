# LeetCode 958 - Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# ✅ Problem:
# A binary tree is complete if every level, except possibly the last, is fully filled,
# and all nodes in the last level appear as far left as possible.
# Return True if the binary tree is complete.

# 📚 Pattern:
# BFS (Level Order Traversal)

# 🔍 Key Insight:
# - Perform level-order traversal (BFS)
# - Once we encounter a `None` (missing child), all nodes after it in BFS must also be None.
# - If any non-None node appears after we've seen a None, the tree is NOT complete.

# 🧠 Memory Hook:
# bfs queue → once you see None, set seen_null = True
# if later you see real node → break rule → return False

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n) for the queue

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seen_null = False  # becomes True after we see the first None (gap)

        while queue:
            node = queue.popleft()

            if node is None:
                # ❗ A gap in the tree — from now on, we should only see more None
                seen_null = True
            else:
                if seen_null:
                    # 🚨 We saw a None earlier, but now see a real node.
                    # This violates completeness — all real nodes must come before the first gap.
                    return False
                # Keep traversing children
                queue.append(node.left)
                queue.append(node.right)

        # ✅ If we never see a real node after a None, it's a complete tree
        return True


# 🔄 Dry Run Example:
# Tree = [1,2,3,4,5,6]
# Level order: 1 → 2 → 3 → 4 → 5 → 6 → None → None ...
# No real node after None → returns True ✅