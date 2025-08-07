# LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

"""
✅ Problem:
You have an undirected tree with n nodes labeled 0 to n - 1.  
It is given as an array edges where edges[i] = [ai, bi] means
there is an edge between nodes ai and bi.  
You also have a boolean array hasApple, where hasApple[i] = True means node i has an apple.  

Time to traverse one edge = 1 second.
Return the minimum time needed to collect all apples and return to node 0.

📚 Pattern:
Tree DFS (post-order) + "useful edge" counting

🔍 Key Insight:
- Only traverse edges that lead to at least one apple.
- Each "useful" edge costs 2 seconds (go + return).
- DFS returns the total time for the subtree; parent decides whether to add +2 for that edge.

🧠 Memory Hook:
"Useful edge → +2 seconds"
(Go + return, only if subtree has an apple)

✅ Time Complexity: O(n) — visit each node once
✅ Space Complexity: O(n) — adjacency list + recursion stack
"""

from typing import List
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build undirected adjacency list
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node: int, parent: int) -> int:
            """
            Returns total time needed to collect apples in this node's subtree
            and come back to 'node'.
            """
            time = 0
            for nei in g[node]:
                if nei == parent:  # avoid going back up
                    continue
                child_time = dfs(nei, node)
                # If child's subtree has apples (child_time > 0) OR child itself has an apple,
                # then edge (node <-> nei) is "useful" → add child's time + 2 seconds.
                if child_time > 0 or hasApple[nei]:
                    time += child_time + 2
            return time

        return dfs(0, -1)


"""
🔄 Dry Run Example:
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False, False, True, False, True, True, False]

DFS steps:
- Start at 0:
    - Go to 1:
        - Go to 4 → hasApple[4] = True → return 0 to 1, add +2 at 1
        - Go to 5 → hasApple[5] = True → return 0 to 1, add +2 at 1
        => total from 1's subtree = 4
        => edge 0-1 → + (4 + 2) = 6
    - Go to 2:
        - hasApple[2] = True → no deeper travel
        => edge 0-2 → +2
Total time = 8
"""