# LeetCode 129 - Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# ✅ Problem:
# You're given a binary tree where each node contains a digit (0-9).
# Each root-to-leaf path forms a number.
# Return the **sum** of all these numbers.

# 🔍 Key Insight:
# - Use **DFS traversal**.
# - At each node, pass down the current number formed so far.
# - When you reach a leaf, add that number to the total sum.

# ✅ Time Complexity: O(n) — Visit every node once
# ✅ Space Complexity: O(h) — Recursion stack, h = height of tree

# 📚 Pattern: DFS (Preorder traversal)

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum = curr_sum * 10 + node.val
            
            # If it's a leaf, return the full number
            if not node.left and not node.right:
                return curr_sum
            
            # Recurse left and right
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        return dfs(root, 0)

# 🔄 Dry Run:
# Input: [1,2,3]
# Path 1→2 → 12
# Path 1→3 → 13
# Output = 12 + 13 = 25

# 🧠 Follow-up:
# - You can also solve this iteratively using a stack: [(node, path_so_far)]
# - Useful for converting a tree path into numerical values

# 📌 Common Gotchas:
# - Remember to multiply by 10 at each level to shift digits
# - Handle leaf node correctly: return curr_sum only when both children are None