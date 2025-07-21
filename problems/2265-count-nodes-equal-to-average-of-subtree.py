# LeetCode 2265 - Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# ✅ Problem:
# Given the root of a binary tree, return the number of nodes where the value of the node
# is equal to the **integer average** of its subtree (including the node itself).

# 📚 Pattern:
# DFS - Postorder Traversal

# 🔍 Key Insight:
# - For each node, you need:
#   (1) sum of its entire subtree
#   (2) number of nodes in its subtree
# - Then: check if node.val == sum // count
# - Must return (sum, count) upward — typical bottom-up recursion

# 🧠 Memory Hook:
# postorder DFS
# get (sum, count) from left + right
# check: node.val == total_sum // total_count → count += 1

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(h) - height of the tree (O(log n) avg, O(n) worst)

# 📌 Common Gotchas:
# - Must use integer division: `//`, not `/`
# - Don't forget to include the current node in the subtree's sum/count
# - Return both sum and count upward to parent calls

# -------------------------------
# ✅ Clean DFS Post-order Solution
# -------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0  # Global counter for result

        # 🧭 Post-order DFS: returns (sum, count) of subtree
        def dfs(node):
            if not node:
                return (0, 0)

            # 🪜 Step 1: Recurse on left and right
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            # 🧮 Step 2: Compute current subtree sum and count
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # ✅ Step 3: Check average condition
            if node.val == total_sum // total_count:
                self.count += 1

            return (total_sum, total_count)

        dfs(root)
        return self.count

# 🔄 Dry Run:
# Tree:
#     4
#    / \
#   8   5
#  / \   \
# 0   1   6
#
# - Node 0: avg = 0 → ✅
# - Node 1: avg = 1 → ✅
# - Node 6: avg = 6 → ✅
# - Node 8: [8,0,1] → sum = 9, count = 3 → avg = 3 ≠ 8 ❌
# - Node 5: [5,6] → sum = 11, count = 2 → avg = 5 ✅
# - Node 4: all nodes → sum = 24, count = 7 → avg = 3 ≠ 4 ❌
# → ✅ Final count = 4