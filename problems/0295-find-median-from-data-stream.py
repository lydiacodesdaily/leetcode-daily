# LeetCode 295 - Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# ✅ Problem:
# Design a data structure that supports adding numbers and finding the median efficiently.
# Implement the MedianFinder class:
# - addNum(int num): Adds a number to the data structure.
# - findMedian(): Returns the median of all elements so far.

# 📚 Pattern: Two Heaps (Max-Heap + Min-Heap)

# 🔍 Core Idea:
# - Use two heaps:
#   - Max-heap (invert values for Python's min-heap) to store the smaller half
#   - Min-heap to store the larger half
# - Ensure: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1

# 🧠 Memory Hook:
# two heaps → left = max heap, right = min heap  
# balance after each insert  
# median = avg of roots (even), or root of max heap (odd)

# ✅ Time Complexity:
# - addNum: O(log n)
# - findMedian: O(1)

# ✅ Space Complexity: O(n) for storing all elements

import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (invert values for Python)
        self.left = []  # Holds smaller half
        # Min-heap
        self.right = []  # Holds larger half

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (invert value to simulate max-heap)
        heapq.heappush(self.left, -num)

        # Step 2: Balance - move the max of left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: Maintain size property
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0

# 🔄 Example:
# mf = MedianFinder()
# mf.addNum(1)
# mf.addNum(2)
# mf.findMedian() -> 1.5
# mf.addNum(3)
# mf.findMedian() -> 2.0