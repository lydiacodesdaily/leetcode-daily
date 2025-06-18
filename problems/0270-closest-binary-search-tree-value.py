# LeetCode 270 - Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/

# ✅ Problem:
# Given a binary search tree (BST) and a target value,
# return the value in the BST that is closest to the target.
# If multiple values are equally close, return the **smaller** one.

# 📚 Pattern:
# Binary Search on BST (Iterative)

# 🔍 Key Insight:
# BST property allows pruning: 
# - If target < node.val → go left
# - If target > node.val → go right
# - At each node, compare current node’s value to closest seen so far

# 🧠 Memory Hook:
# track `closest` seen so far
# update if abs(node.val - target) < abs(closest - target)
# search BST like binary search

# ✅ Time Complexity: O(h), where h is the height of the tree
# ✅ Space Complexity: O(1) – iterative, no recursion

# 📌 Common Gotchas:
# - Forgetting to update closest only on *strictly smaller* diff
# - If equal diff, return the smaller value

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        
        while root:
            # 🧮 Update closest if this node is closer to target
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)

            # 🧭 Navigate BST
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest

# 🔄 Dry Run:
# Input: root = [4,2,5,1,3], target = 3.714286
# Path: 4 → 2 → 3
# Closest values checked: 4, 2, 3 → Best match = 4 (diff = 0.285714)

# 🎯 Final Output: 4