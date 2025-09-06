# LeetCode 94 - Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# ✅ Problem:
# Given the root of a binary tree, return its inorder traversal.
# Inorder = Left → Node → Right

# 📚 Pattern:
# Binary Tree DFS Traversal (Inorder)

# 🔍 Core Idea:
# Use recursion or stack to simulate "left → node → right" visiting order.

# 🧠 Memory Hook:
# inorder = left → node → right
# recursive: dfs(left), add node, dfs(right)
# iterative: push left, pop, visit, go right

# ✅ Time Complexity: O(n)  (visit each node once)
# ✅ Space Complexity: O(h) recursion stack or iterative stack, h = height of tree

# 📌 Common Gotchas:
# - Forgetting to append node value in correct position
# - Not moving to right subtree after visiting a node in iterative version

# ---------------- Recursive Version ----------------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            # Step 1: Traverse left
            dfs(node.left)
            # Step 2: Visit node
            result.append(node.val)
            # Step 3: Traverse right
            dfs(node.right)

        dfs(root)
        return result


# ---------------- Iterative Version ----------------
class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        # skeleton: go left as far as possible, then pop + visit, then go right
        while curr or stack:
            # Step 1: Push all left nodes
            while curr:
                stack.append(curr)
                curr = curr.left
            # Step 2: Pop + visit node
            curr = stack.pop()
            result.append(curr.val)
            # Step 3: Move to right child
            curr = curr.right

        return result


# 🔄 Dry Run:
# Input: root = [1,null,2,3]
# Tree:
#     1
#      \
#       2
#      /
#     3
#
# Recursive traversal:
# dfs(1) → dfs(None) → add 1 → dfs(2)
# dfs(2) → dfs(3) → dfs(None) → add 3 → dfs(None) → add 2 → dfs(None)
# Output = [1,3,2] ✅