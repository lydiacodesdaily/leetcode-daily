import heapq
from typing import List

# Leetcode 973 - K Closest Points to Origin
# Use case: Given a list of points, return the k closest points to the origin (0,0)
#
# 🧠 Strategy:
# - Use a max heap of size k to track the closest k points
# - Push negative distance (since heapq is a min-heap by default)
# - Pop from heap if size exceeds k
#
# ⏰ Time Complexity: O(n log k), where n is number of points
# 💾 Space Complexity: O(k) for storing the heap
#
# ❗ Note: We store x**2 + y**2 instead of sqrt(x**2 + y**2) because:
# - The square root function is monotonic
# - It maintains the same order when comparing distances
# - It's more efficient (no need to compute actual square root)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  # max heap by negative squared distance; stores (-distance, point)

        # Calculate distance for each point and add to heap
        for x, y in points:
            distance = x**2 + y**2 # Squared Euclidean distance  
            heapq.heappush(max_heap, (-distance, x, y)) # negate to simulate max-heap
            
            # Remove points if heap size exceeds k
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract k closest points
        return [[x, y] for (_, x, y) in max_heap]

# Dry run example:
# Input: points = [[1,3],[-2,2]], k = 1
# Step 1: Compute squared distances
#   [1,3] -> 1^2 + 3^2 = 10
#   [-2,2] -> (-2)^2 + 2^2 = 8
# Step 2: Use heap to track closest
#   Add (-10, 1, 3)
#   Add (-8, -2, 2) → heap now has 2 elements, pop farthest → pop (-10, 1, 3)
# Step 3: Return remaining in heap → [[-2, 2]]