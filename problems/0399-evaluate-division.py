# LeetCode 399 - Evaluate Division
# https://leetcode.com/problems/evaluate-division/

# ✅ Problem:
# Given equations like a / b = 2.0 and queries like a / c,
# return the value of each query using known equations.
# If not possible, return -1.0.

# 📚 Pattern:
# Weighted Graph Traversal (DFS or BFS)

# 🔍 Key Insight:
# - Treat variables as graph nodes
# - Each equation a / b = k means:
#     graph[a][b] = k, graph[b][a] = 1/k
# - To evaluate a query like x / y:
#     DFS from x to y, multiplying edge weights

# 🧠 Memory Hook:
# graph[a][b] = k
# DFS from x to y → multiply weights along path

# ✅ Time Complexity:
# - Build graph: O(E) where E = number of equations
# - Each query: worst-case O(N) where N = number of variables (nodes)
# ✅ Space Complexity: O(N + E)

from typing import List, Dict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        # Step 1: Build graph
        graph = defaultdict(dict)  # {a: {b: val, ...}, ...}
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        # Step 2: DFS to find path product
        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * weight  # ⬅️ multiply as we return up
            return -1.0

        # Step 3: Process queries
        output = []
        for x, y in queries:
            result = dfs(x, y, set())
            output.append(result)

        return output


# 🔍 Dry Run Example
if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    # Expected: [6.0, 0.5, -1.0, 1.0, -1.0]
    sol = Solution()
    result = sol.calcEquation(equations, values, queries)
    print(result)