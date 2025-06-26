# LeetCode 480 - Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/

# ✅ Problem:
# Given an integer array nums and a sliding window size k, 
# return the median of each sliding window as the window moves from left to right.

# 📚 Pattern: Sliding Window + Two Heaps

# 🔍 Core Idea:
# 1. Brute Force: Maintain the window, sort at each step → O(nk log k)
# 2. Optimal: Use two heaps to maintain order, balance heaps, lazy delete outgoing elements → O(n log k)

# 🧠 Memory Hook:
# Two heaps → max heap (left), min heap (right)
# Insert → balance → lazy remove → balance → get median

# ✅ Time Complexity:
# Brute Force: O(nk log k)
# Optimal: O(n log k)

# ✅ Space Complexity: O(k)

# 📌 Common Gotchas:
# - Forgetting to lazy delete the element that slides out.
# - Misbalancing heaps (left size can only exceed right size by 1).
# - Off-by-one errors when picking the median from heaps.

from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    # Brute Force - Easier to recall for live interview
    def medianSlidingWindow_brute(self, nums, k):
        result = []
        for i in range(len(nums) - k + 1):
            window = sorted(nums[i:i + k])
            if k % 2 == 1:
                result.append(float(window[k // 2]))
            else:
                result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        return result

    # Optimal - Two Heaps with Lazy Deletion
    def medianSlidingWindow_optimal(self, nums, k):
        max_heap = []  # max heap (left side) - store negative values
        min_heap = []  # min heap (right side)
        delayed = defaultdict(int)

        def get_median():
            if k % 2 == 1:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0]) / 2.0

        def balance():
            while len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, -heappop(max_heap))
            while len(max_heap) < len(min_heap):
                heappush(max_heap, -heappop(min_heap))

        def prune(heap):
            while heap and delayed[(heap[0] * (-1 if heap is max_heap else 1))]:
                num = heap[0] * (-1 if heap is max_heap else 1)
                delayed[num] -= 1
                heappop(heap)

        result = []

        # Build initial window
        for i in range(k):
            heappush(max_heap, -nums[i])
        balance()

        result.append(get_median())

        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]

            if in_num <= -max_heap[0]:
                heappush(max_heap, -in_num)
            else:
                heappush(min_heap, in_num)

            delayed[out_num] += 1

            if out_num <= -max_heap[0]:
                if out_num == -max_heap[0]:
                    prune(max_heap)
            else:
                if out_num == min_heap[0]:
                    prune(min_heap)

            balance()
            prune(max_heap)
            prune(min_heap)

            result.append(get_median())

        return result

# 🔄 Dry Run:
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Brute Force: sort each window and pick median
# Optimal: maintain two heaps, insert new element, lazy remove old, balance heaps
