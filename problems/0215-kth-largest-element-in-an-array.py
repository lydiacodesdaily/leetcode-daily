# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
🧠 Pattern: Heap (Min Heap)
🎯 Problem: Find the kth largest element in an unsorted array.
🔍 Insight: Keep a min heap of size k. Pop the smallest whenever size exceeds k.
💡 Time: O(n log k)
💾 Space: O(k)
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min Heap of size k
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Pop smallest

        return min_heap[0]

"""
🧪 Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""