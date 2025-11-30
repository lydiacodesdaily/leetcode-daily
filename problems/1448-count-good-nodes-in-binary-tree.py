# LeetCode 1448 - Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# ✅ Problem:
# A node X in the binary tree is called "good" if on the path from the root to X
# there are no nodes with a value greater than X.val.
# Return the total number of good nodes in the tree.
#
# 📚 Pattern:
# DFS (preorder) with "state" carried along the path (max-so-far)
#
# 🔍 Core Idea:
# - As you traverse from root to leaves, keep track of the maximum value seen so far on that path.
# - A node is "good" if node.val >= max_so_far.
# - Update max_so_far and recurse into left and right children, summing up "good" counts.
#
# 🧠 Memory Hook:
# - pass down path_max in DFS param
# - good if node.val >= path_max
# - update path_max = max(path_max, node.val)
# - result = current_good + left + right
#
# ✅ Time Complexity: O(n)   (visit each node once)
# ✅ Space Complexity: O(h)  (recursion stack height = tree height)
#
# 📌 Common Gotchas:
# - Forgetting to update maxSoFar *before* passing it down to children.
# - Trying to use global vars when a parameter (maxSoFar) is cleaner.
# - Confusing "global max in tree" vs. "max on path from root to this node".
#
# ----------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: 'TreeNode') -> int:
        # DFS
        # T: O(n), S: O(h)

        # 🔹 dfs(node, maxVal): returns number of good nodes in subtree rooted at `node`,
        #                       given the maximum value seen so far on the path.
        def dfs(node, maxVal):
            # 1️⃣ Base case: empty subtree contributes 0 good nodes
            if not node:
                return 0

            # 2️⃣ Process current node: check if it's a "good" node
            #    - good if node.val >= maxVal along the path so far
            res = 1 if node.val >= maxVal else 0

            # 3️⃣ Update path state: new max for children is the max of (maxVal, node.val)
            maxVal = max(maxVal, node.val)

            # 4️⃣ Recurse into children with updated maxVal
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            # 5️⃣ Return total count of good nodes from this subtree
            return res

        # Edge case: if root is None, there are no nodes at all (0 good nodes)
        if root is None:
            return 0

        # Start DFS from the root; initial maxVal is root.val (root is always good)
        return dfs(root, root.val)


# ----------------------------------------------------------------------
# 🔄 Dry Run Example
#
# Example tree:
#        3
#       / \
#      1   4
#     /   / \
#    3   1   5
#
# Path checks:
# - Path to 3 (root): [3]          → max so far = 3 → 3 >= 3  → good
# - Path to 1 (left): [3, 1]       → max so far = 3 → 1 < 3   → not good
# - Path to 3 (left-left): [3, 1, 3] → max so far = 3 → 3 >= 3 → good
# - Path to 4 (right): [3, 4]      → max so far = 3 → 4 >= 3  → good
# - Path to 1 (right-left): [3, 4, 1] → max so far = 4 → 1 < 4 → not good
# - Path to 5 (right-right): [3, 4, 5] → max so far = 4 → 5 >= 4 → good
#
# Good nodes: 3 (root), 3 (left-left), 4, 5 → total = 4
#
# dfs(root=3, maxVal=3):
#   node=3 → good (3 >= 3) → res=1, maxVal=3
#     dfs(1, maxVal=3):
#       node=1 → not good (1 < 3) → res=0, maxVal=3
#         dfs(3, maxVal=3):
#           node=3 → good (3 >= 3) → res=1, maxVal still=3
#             dfs(None, 3) → 0
#             dfs(None, 3) → 0
#           return 1
#         dfs(None, 3) → 0
#       return 1
#     dfs(4, maxVal=3):
#       node=4 → good (4 >= 3) → res=1, maxVal=4
#         dfs(1, maxVal=4):
#           node=1 → not good (1 < 4) → res=0, maxVal=4
#             dfs(None, 4) → 0
#             dfs(None, 4) → 0
#           return 0
#         dfs(5, maxVal=4):
#           node=5 → good (5 >= 4) → res=1, maxVal=5
#             dfs(None, 5) → 0
#             dfs(None, 5) → 0
#           return 1
#       return 2
#   Total = 1 (root) + 1 (left subtree) + 2 (right subtree) = 4