# LeetCode 787 - Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# ✅ Problem:
# Given n cities and a list of flights (edges with cost),
# find the cheapest price from src to dst with at most k stops.
# If not possible, return -1.

# 📚 Pattern:
# Dijkstra with additional constraint (stop count)
# - Track (cost, node, stops) in min-heap
# - Similar to BFS with pruning via priority queue

# 🔍 Core Idea:
# Use min-heap to always expand the cheapest cost path first.
# Track number of stops used, and prune paths that exceed k.

# 🧠 Memory Hook:
# min-heap = (cost, node, stops)
# push neighbor only if stops <= k
# skip path if we've seen the node with fewer stops already

# ✅ Time Complexity: O(E + V log V) (bounded by total flights)
# ✅ Space Complexity: O(V + E)

# 📌 Common Gotchas:
# - Don’t early return just because dst is seen — it may not be cheapest yet
# - Be careful with stop count (<= k, not < k)
# - Use visited[node] = min stops so far to prune worse paths

from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Step 1: Build graph as adjacency list
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        # Step 2: Min-heap for Dijkstra-like traversal
        # (cost so far, current node, stops used)
        heap = [(0, src, 0)]

        # Step 3: Track visited nodes with their minimum stop count
        visited = {}

        while heap:
            cost, city, stops = heapq.heappop(heap)

            # ✅ If destination reached, return current cost
            if city == dst:
                return cost

            # Prune if we've seen this node with fewer stops
            if city in visited and visited[city] <= stops:
                continue
            visited[city] = stops

            # Expand neighbors only if within stop limit
            if stops <= k:
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1

# 🔄 Dry Run:
# Input:
# n = 4
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1

# Graph: { 0: [(1,100), (2,500)], 1: [(2,100)] }

# Min-heap = [(0, 0, 0)]  # (cost, city, stops)
# visited = {}

# 1st pop → (0, 0, 0)
#   neighbors:
#     (1, 100) → push (100, 1, 1)
#     (2, 500) → push (500, 2, 1)
# heap = [(100, 1, 1), (500, 2, 1)]

# 2nd pop → (100, 1, 1)
#   neighbor:
#     (2, 100) → push (200, 2, 2)
# heap = [(200, 2, 2), (500, 2, 1)]

# 3rd pop → (200, 2, 2)
#   ✅ destination reached with cost = 200
# return 200