# LeetCode 215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# ✅ Problem:
# Given an integer array `nums` and an integer `k`,
# return the k-th largest element in the array.
# (Note: It's the k-th largest **number**, not its index.)

# 📚 Pattern:
# Heap (Min-Heap of size k)

# 🔍 Core Idea:
# Maintain a min-heap with the k largest elements seen so far.
# The top of the heap is the k-th largest overall.

# 🧠 Memory Hook:
# heapq = min-heap → store k largest
# push new num → pop smallest if len > k
# kth largest = top of heap

# ✅ Time Complexity:
# O(n log k) — inserting into heap of size k
# ✅ Space Complexity:
# O(k) — size of heap

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

# 🔄 Dry Run:
# nums = [3,2,1,5,6,4], k = 2
# Min-heap evolution:
# [3]
# [2,3]
# [1,3,2] → pop 1 → [2,3]
# [2,3,5] → pop 2 → [3,5]
# [3,5,6] → pop 3 → [5,6]
# [4,6,5] → pop 4 → [5,6]
# ✅ kth largest = 5

# 📌 Common Gotchas:
# - Off-by-one confusion: make sure you're returning the k-th *largest*, not smallest
# - Don’t sort the array if asked for better than O(n log n)