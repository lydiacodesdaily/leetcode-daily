# ===============================================================
# LeetCode 124 - Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# ===============================================================

# ✅ Problem:
# A *path* is any sequence of nodes connected parent → child.
# It may start and end anywhere in the tree.
#
# Find the maximum sum of **any** path.
# A path may:
#   - include the root or not
#   - turn at a node (left + node + right)
#   - be just a single node
#
# Nodes may have negative values.

# 📚 Pattern:
# DFS (Postorder) + "max gain from child" return strategy

# 🔍 Core Idea:
# At each node:
#   • Compute best downward path (single-branch gain)
#   • Compute best *turning* path (left + node + right)
#   • Update global max with the turning path
#   • Return node.val + max(leftGain, rightGain)

# 🧠 Memory Hook:
# - child gain can't be negative → cap at 0  
# - global_max gets (L + node + R)  
# - return upward: node + max(L, R) (single branch only)

# ⏱ Time Complexity: O(n)
# 📦 Space Complexity: O(h) recursion depth

# =================================================================
# 🧩 Structural Steps (inside code)
# 1. dfs(node):
#       a. base case
#       b. compute left/right gains
#       c. clamp negatives to 0
#       d. compute turning path (L + node + R)
#       e. update global max
#       f. return upward gain (node + max(L, R))
# =================================================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        # global max stored in list for mutability
        res = [root.val]

        def dfs(node):
            # --------------------------
            # 1. Base case
            # --------------------------
            if not node:
                return 0

            # --------------------------
            # 2. DFS children
            # --------------------------
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # --------------------------
            # 3. Clamp negatives:
            #    A negative gain will only reduce path sum,
            #    so treat as 0 (do not include that branch)
            # --------------------------
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # --------------------------
            # 4. Turning path at node:
            #    best path THROUGH this node
            # --------------------------
            currPath = node.val + leftMax + rightMax

            # --------------------------
            # 5. Update global maximum
            # --------------------------
            res[0] = max(res[0], currPath)

            # --------------------------
            # 6. Return best single-branch gain upward
            # --------------------------
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]


# ===============================================================
# 🔄 Dry Run Example
# ---------------------------------------------------------------
#      -10
#      /  \
#     9   20
#         / \
#        15  7
#
# left gains:
#   9 → return 9
# right gains:
#   15 → return 15
#   7  → return 7
#
# At node 20:
#   currPath = 20 + 15 + 7 = 42   ← global max updated
#   return upward = 20 + max(15,7) = 35
#
# At node -10:
#   currPath = -10 + 9 + 35 = 34  (but global max stays 42)
#
# Final answer = 42
# ===============================================================