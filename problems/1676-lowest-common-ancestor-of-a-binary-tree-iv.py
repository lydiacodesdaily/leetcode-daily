# LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

# ✅ Problem:
# Given the root of a binary tree and a list of TreeNode objects,
# return their **lowest common ancestor (LCA)**.
# All nodes are guaranteed to exist in the tree and have unique values.

# 📚 Pattern:
# Post-order DFS (Bottom-Up)
# - Extend the classic LCA (236) logic to support **multiple nodes**
# - Track presence of targets using a set for O(1) lookup

# 🔍 Key Insight:
# - For each node:
#   - If node is in targets → return it
#   - Recurse left and right
#   - If both left and right return non-null → this is the LCA
#   - Otherwise, bubble up non-null child result

# 🧠 Memory Hook:
# - targets = set(nodes)
# - if node in targets → return node
# - if left and right → return node
# - return left or right
# → Classic LCA logic with multiple inputs

# ✅ Time Complexity: O(n) — traverse entire tree
# ✅ Space Complexity: O(h + t) — recursion stack (height h) + set of targets (t)

# 📌 Common Gotchas:
# - Forgetting to convert nodes to a set
# - Not handling >2 targets properly
# - Assuming sorted or balanced tree (nope!)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: List['TreeNode']) -> 'TreeNode':
        # ✅ Convert list to set for O(1) lookup
        target_set = set(nodes)

        def dfs(node):
            if not node:
                return None

            # 🎯 Base case: if this node is in target list, return it
            if node in target_set:
                return node

            # 🔁 Recurse left and right
            left = dfs(node.left)
            right = dfs(node.right)

            # 🧭 If both children return non-null, this node is the LCA
            if left and right:
                return node

            # 🪜 Otherwise, bubble up whichever is non-null
            return left or right

        return dfs(root)

# 🔄 Dry Run:
# Tree:
#        3
#       / \
#      5   1
#     / \
#    6   2
# Targets = [6, 2]
# dfs(6) → 6
# dfs(2) → 2
# dfs(5) gets left=6, right=2 → return 5 ✅
# dfs(3) gets left=5, right=None → return 5