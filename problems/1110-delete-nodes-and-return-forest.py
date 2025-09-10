# LeetCode 1110 - Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/

# 📚 Pattern:
# DFS with parent-child link updates + forest collection

# 🔍 Key Insight:
# - Treat "delete" as cutting the link from its parent.
# - If a deleted node has children → those children become new roots.
# - The first call starts with root=True to consider original root.

# 🧠 Memory Hook:
# "Delete? → cut link + promote children"
# If parent deleted → child becomes root in result.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None
            
            # Is this node deleted?
            deleted = node.val in to_delete_set

            # If it's a root and not deleted → add to forest
            if is_root and not deleted:
                forest.append(node)

            # Recurse on children
            node.left = dfs(node.left, deleted)   # child becomes root if current is deleted
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return forest