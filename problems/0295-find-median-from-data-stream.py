# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

"""
🧠 Pattern: Two Heaps (Max Heap + Min Heap)
🎯 Problem: Continuously receive numbers and find the median efficiently.
📌 Use Cases:
- Real-time data feeds (e.g., stock prices, sensor data)
- Rolling statistical calculations
- Streaming analytics

⏰ Time Complexity:
- addNum(): O(log n)
- findMedian(): O(1)

📦 Space Complexity: O(n), where n is number of inserted elements
"""

import heapq

class MedianFinder:

    def __init__(self):
        # Max heap (lower half) — store as negative numbers
        self.max_heap = []  # Python heapq is a min-heap, so negate values
        # Min heap (upper half)
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max_heap (as negative to simulate max-heap)
        heapq.heappush(self.max_heap, -num)

        # Step 2: Move the largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Step 3: Balance sizes so max_heap can have 1 more element
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If total count is odd → max_heap has the median
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        # If even → average of roots of both heaps
        return (-self.max_heap[0] + self.min_heap[0]) / 2


"""
🧪 Example Usage:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2.0
"""