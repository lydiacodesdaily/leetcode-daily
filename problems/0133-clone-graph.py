from typing import Optional

# LeetCode 133: Clone Graph
# Problem: Given a reference of a node in a connected undirected graph,
# return a deep copy (clone) of the graph.
#
# Use Case: Clone complex graphs with cycles or shared nodes (e.g., in networking, compilers).
# Pattern: Graph traversal with DFS + Hashmap
#
# Time Complexity: O(N) where N is the number of nodes + edges
# Space Complexity: O(N) due to visited hashmap and recursion stack

class Node:
    def __init__(self, val: int, neighbors: list['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # Maps original node -> cloned node

        def dfs(curr):
            if curr in visited:
                return visited[curr]  # Return clone if already visited

            # Clone the current node (without neighbors yet)
            clone = Node(curr.val)
            visited[curr] = clone

            # Recursively clone all neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

# Example Dry Run:
# Graph:
# 1 -- 2
# |    |
# 4 -- 3
# Start at node 1:
# clone 1, recurse into 2 -> clone 2, recurse into 3 -> clone 3, recurse into 4 -> clone 4
# All nodes visited and cloned, cycle handled via "visited" hashmap

# To test:
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.neighbors = [node2, node4]
# node2.neighbors = [node1, node3]
# node3.neighbors = [node2, node4]
# node4.neighbors = [node1, node3]
# cloned = Solution().cloneGraph(node1)

"""
🧪 Dry Run Example:

Input Graph:
1 -- 2
|    |
4 -- 3

Let node = Node(1)

Step-by-step:
- Call dfs(1): not visited → clone 1 → visited[1] = clone1
- For neighbor 2:
  - Call dfs(2): not visited → clone 2 → visited[2] = clone2
  - For neighbor 3:
    - Call dfs(3): not visited → clone 3 → visited[3] = clone3
    - For neighbor 4:
      - Call dfs(4): not visited → clone 4 → visited[4] = clone4
      - 4 connects to 1 (already visited): reuse clone1
    - clone3 connects to clone4
  - clone2 connects to clone3
- For neighbor 4:
  - 4 already visited: reuse clone4
- clone1 connects to clone2 and clone4

✅ Final cloned structure matches the original.

🕒 Time Complexity: O(N), where N = total nodes + edges
📦 Space Complexity: O(N), due to hashmap + recursion stack
"""
