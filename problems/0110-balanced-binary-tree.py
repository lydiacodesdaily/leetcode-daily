# LeetCode 110 - Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# 📚 Pattern:
# Postorder DFS (compute child info → use it to compute parent)

# 🔍 Core Idea:
# At each node, compute:
#   (1) is the subtree balanced?
#   (2) what is its height?

# 🧠 Memory Hook:
# postorder dfs
# return (balanced, height)
# balanced = both balanced + |lh - rh| ≤ 1
# height = 1 + max(lh, rh)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(h)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        # ============================================================
        # dfs(node) returns a tuple: (is_balanced: bool, height: int)
        #
        # Structure:
        # 1. Base case
        # 2. Recurse left & right (postorder)
        # 3. Check if current node is balanced
        # 4. Compute height
        # 5. Return tuple explicitly
        # ============================================================
        def dfs(node):
            # -------- 1. Base case --------
            if not node:
                return (True, 0)

            # -------- 2. Postorder: compute left & right first --------
            (left_balanced, left_height) = dfs(node.left)
            (right_balanced, right_height) = dfs(node.right)

            # -------- 3. Balance check --------
            is_balanced_here = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            # -------- 4. Height calc --------
            height_here = 1 + max(left_height, right_height)

            # -------- 5. Explicit tuple return --------
            return (is_balanced_here, height_here)

        (balanced, _) = dfs(root)
        return balanced


# ---------------------------------------------------------------
# 📌 Example:
#
# #       3
# #      / \
# #     9  20
# #        / \
# #       15  7
#
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))
#
# print(Solution().isBalanced(root))  # True
#
# ---------------------------------------------------------------