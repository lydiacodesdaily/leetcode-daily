# LeetCode 297 - Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# 📚 Pattern: Binary Tree DFS (Preorder)
# - Use DFS to record values in preorder traversal: root → left → right
# - Use "N" as null markers so the structure can be reconstructed
#
# 🔍 Core Idea:
# Serialize: preorder DFS + store "N" for nulls
# Deserialize: read list using index pointer; rebuild tree in preorder order
#
# 🧠 Memory Hook:
# "preorder list"
# "N for null"
# "index pointer moves forward"
# "build: node → left → right"
#
# ✅ Time Complexity:
# - Serialize: O(n)
# - Deserialize: O(n)
#   (each node visited once)
#
# ✅ Space Complexity:
# - O(n) for output list + recursion stack


# ------------------------------------------------------------
# Definition for a binary tree node.
# ------------------------------------------------------------
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# ------------------------------------------------------------
# Codec Class
# ------------------------------------------------------------
class Codec:

    # --------------------------------------------------------
    # 🔸 Serialize: Tree → String
    # --------------------------------------------------------
    # Strategy:
    # 1. Preorder DFS: append node values
    # 2. Append "N" for null children
    # 3. Join with commas
    #
    # Example:
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    #
    # serialize → "1,2,N,N,3,4,N,N,5,N,N"
    # --------------------------------------------------------
    def serialize(self, root):
        res = []

        def dfs(node):
            # Base case: null
            if not node:
                res.append("N")
                return

            # Preorder: root → left → right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)


    # --------------------------------------------------------
    # 🔸 Deserialize: String → Tree
    # --------------------------------------------------------
    # Strategy:
    # 1. Split string into array
    # 2. Use pointer `self.i` to rebuild tree in preorder
    # 3. If token == "N": return None
    #
    # Example:
    # "1,2,N,N,3,4,N,N,5,N,N"
    #
    # dfs() call order rebuilds exact shape.
    # --------------------------------------------------------
    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0  # pointer over vals

        def dfs():
            # If null marker → return None
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Build node
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # Rebuild left subtree
            node.left = dfs()

            # Rebuild right subtree
            node.right = dfs()

            return node

        return dfs()


# ------------------------------------------------------------
# Example usage:
# ------------------------------------------------------------
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))