# LeetCode 863 - All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# ✅ Problem:
# Given the root of a binary tree, a target node, and an integer k,
# return all the values of the nodes that are a distance k from the target node.
#
# Nodes can be reached by going up (parent), left, or right.

# 📚 Pattern:
# BFS from Target + DFS Preprocessing (Parent Map)

# 🔍 Core Idea:
# 1. Traverse the tree to build a map from each node to its parent.
# 2. Do BFS from the target node, treating the tree like an undirected graph (left, right, parent).
# 3. Stop when distance == k.

# 🧠 Memory Hook:
# dfs → build parent map
# bfs from target, track seen
# stop when dist == k → collect all nodes

# ✅ Time Complexity: O(n) — visit all nodes once
# ✅ Space Complexity: O(n) — parent map + queue + seen set

from collections import deque

class Solution:
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
        parent = {}

        # Step 1: DFS to record each node's parent
        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Step 2: BFS from target to find nodes at distance k
        queue = deque([(target, 0)])
        seen = {target}
        res = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                res.append(node.val)
            elif dist < k:
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return res

# 🔄 Dry Run:
# Tree: [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Step 1: Build parent links: {6:5, 2:5, 0:1, 8:1, ...}
# Step 2: BFS from 5 → at distance 2: nodes 7, 4, 1
# Output: [7, 4, 1]