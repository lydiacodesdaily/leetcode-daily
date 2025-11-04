# LeetCode 239 - Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

# ✅ Problem:
# You are given an integer array nums and an integer k.
# There is a sliding window of size k moving from left to right.
# Return the maximum value in each window.

# 📚 Pattern:
# Monotonic Deque (Decreasing)

# 🔍 Core Idea:
# Use a deque to store indices of elements in decreasing order of their values.
# - The front of the deque always holds the index of the max element in the window.
# - Pop smaller elements from the back to maintain decreasing order.
# - Pop left if the element falls out of the window range (i - k).

# 🧠 Memory Hook:
# deque ↓ decreasing order
# pop back smaller
# pop left if out of range
# front → max of window

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(k)

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 🧱 Initialize deque (store indices) and result array
        queue = deque()
        res = []

        # 🪟 Step 1: Process the first k elements (first window)
        for i in range(k):
            # Maintain decreasing order: remove all smaller values from the back
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

        # Append max of first window
        res.append(nums[queue[0]])

        # 🚀 Step 2: Slide the window through the rest of the array
        for i in range(k, len(nums)):
            # 1️⃣ Remove elements that fall out of the window (i - k)
            if queue and queue[0] == i - k:
                queue.popleft()

            # 2️⃣ Maintain decreasing order
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # 3️⃣ Append current window's maximum (front of deque)
            res.append(nums[queue[0]])

        return res


# 🔄 Dry Run:
# nums = [1,3,-1,-3,5,3,6,7], k = 3
# Window 1: [1,3,-1] → max=3
# Window 2: [3,-1,-3] → max=3
# Window 3: [-1,-3,5] → max=5
# Window 4: [-3,5,3] → max=5
# Window 5: [5,3,6] → max=6
# Window 6: [3,6,7] → max=7
# ✅ Output: [3,3,5,5,6,7]