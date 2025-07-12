# LeetCode 536 - Construct Binary Tree from String
# https://leetcode.com/problems/construct-binary-tree-from-string/

# ✅ Problem:
# You are given a string s that represents a binary tree:
# - Each integer node is followed by zero, one, or two pairs of parentheses.
# - The first pair contains the left child, the second the right child.
# Return the binary tree represented by this string.

# 📚 Pattern:
# Recursion + String Parsing

# 🔍 Key Insight:
# - We use recursion to build the tree.
# - At each step, extract the current root value, then parse left and right subtrees.

# 🧠 Memory Hook:
# "Value (left) (right)" → parse root → recursively build children
# Use a helper function with index tracking to avoid repeated slicing.

# ✅ Time Complexity: O(n), where n = length of string (each character processed once)
# ✅ Space Complexity: O(h), where h = height of tree (due to recursion stack)

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        def parse(index):
            # Step 1: Parse number (can be negative)
            is_negative = False
            if s[index] == '-':
                is_negative = True
                index += 1
            num = 0
            while index < len(s) and s[index].isdigit():
                num = num * 10 + int(s[index])
                index += 1
            val = -num if is_negative else num
            node = TreeNode(val)

            # Step 2: Parse left child if exists
            if index < len(s) and s[index] == '(':  # left subtree
                index += 1  # skip '('
                node.left, index = parse(index)
                index += 1  # skip ')'

            # Step 3: Parse right child if exists
            if index < len(s) and s[index] == '(':  # right subtree
                index += 1  # skip '('
                node.right, index = parse(index)
                index += 1  # skip ')'

            return node, index

        root, _ = parse(0)
        return root

# 🔄 Dry Run:
# Input: "4(2(3)(1))(6(5))"
# Output Tree:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5

# 🔹 Notes:
# - We pass `index` to avoid excessive string slicing (efficient!)
# - You can add debug prints inside parse() to understand tree building step-by-step

# 🔸 Common Pitfall:
# - Forgetting to handle negative numbers correctly
# - Not incrementing index after closing ')'
