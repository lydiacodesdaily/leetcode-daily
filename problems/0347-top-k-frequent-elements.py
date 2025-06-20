# LeetCode 347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# ✅ Problem:
# Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
# You must solve it in better than O(n log n) time.

# 🔍 Key Insight:
# Use a **hashmap** to count frequency and a **heap** to extract top `k` elements efficiently.

# 🧠 Memory Hook:
# build freq map → Counter(nums)
# push (count, num) into min-heap → size > k → pop smallest
# return only elements → [num for count, num in heap]

# ✅ Time Complexity:
# - O(n) to count frequencies
# - O(n log k) to maintain a heap of size k
# => Better than O(n log n)

# ✅ Space Complexity: O(n) — for the frequency map and heap

# 📚 Pattern: Hash Map + Heap (Min-Heap of size k)

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Use a min-heap of size k to keep the top k frequent elements
        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract the elements from the heap
        return [num for count, num in min_heap]

# 🔁 Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Frequencies: {1:3, 2:2, 3:1}
# Min-heap after processing: [(2,2), (3,1)]
# Return: [2,1] (or [1,2]) — order doesn’t matter

# 📌 Common Gotchas:
# - Forgetting to return just the elements (not (count, num))
# - Using a max-heap instead of min-heap (can be done by negating count)

# 🧠 Alternative:
# - Bucket Sort: O(n) time, but heap is cleaner and more intuitive for interviews