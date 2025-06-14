from typing import Optional, List
from collections import deque

# LeetCode 199. Binary Tree Right Side View
# 
# Problem:
# Given the root of a binary tree, imagine standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Use case:
# - Visualizing the tree from the right side, such as rendering view or layered tree data.
#
# Approach:
# - Use BFS level-order traversal.
# - For each level, only record the last node processed (rightmost node).
#
# Time Complexity: O(n) where n is number of nodes
# Space Complexity: O(w) where w is max width of tree (can be up to n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    queue = deque([root])

    # Begin level-order traversal (BFS)
    while queue:
        level_length = len(queue)

        # Process all nodes at the current level
        for i in range(level_length):
            node = queue.popleft()

            # Dry run example comment: If we're at the last node of the level, add it to result
            if i == level_length - 1:
                res.append(node.val)

            # Push child nodes into queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res

# Dry run example:
# Tree:
#     1
#    / \
#   2   3
#    \    \
#     5    4
#
# Level 0 → [1] → add 1
# Level 1 → [2, 3] → add 3
# Level 2 → [5, 4] → add 4
# Output: [1, 3, 4]
