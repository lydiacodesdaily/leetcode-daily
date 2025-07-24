# LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

# ✅ Problem:
# Given the root of a binary tree and two nodes `p` and `q`,
# return their lowest common ancestor **only if both nodes exist in the tree**.
# If either `p` or `q` is missing, return `None`.

# 📚 Pattern:
# Postorder DFS (Bottom-Up)
# - Check left and right recursively
# - Add existence flags for `p` and `q` since they might not be in the tree

# 🔍 Key Insight:
# You need to track:
# 1. The LCA node
# 2. Whether p exists in the current subtree
# 3. Whether q exists in the current subtree

# 🧠 Memory Hook:
# - return (lca, found_p, found_q)
# - LCA only valid if both found_p and found_q
# - if left and right both return non-null → LCA = node
# - if node == p or q → return that node

# ✅ Time Complexity: O(n) — visit each node once
# ✅ Space Complexity: O(h) — recursion stack (h = height)

# 📌 Common Gotchas:
# - Forgetting to return flags
# - Returning LCA even if one node is missing
# - Confusing with 236: 1644 requires validation

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return (None, False, False)

            left_lca, left_p, left_q = dfs(node.left)
            right_lca, right_p, right_q = dfs(node.right)

            found_p = left_p or right_p or node == p
            found_q = left_q or right_q or node == q

            # 🎯 If current node is one of the targets
            if node == p or node == q:
                return (node, found_p, found_q)

            # 🧭 If both sides return non-null LCAs → this is the split point
            if left_lca and right_lca:
                return (node, found_p, found_q)

            # 🪜 Otherwise, bubble up the non-null LCA if any
            if left_lca:
                return (left_lca, found_p, found_q)
            if right_lca:
                return (right_lca, found_p, found_q)

            return (None, found_p, found_q)

        lca, found_p, found_q = dfs(root)
        return lca if found_p and found_q else None

# 🔄 Dry Run:
# Tree:       3
#            / \
#           5   1
# p = 5, q = 42 (not in tree)
# → dfs(3)
#   → dfs(5) → returns (5, True, False)
#   → dfs(1) → returns (None, False, False)
# → returns (5, True, False) → ❌ not both found → return None ✅