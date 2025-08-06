# LeetCode 1011 - Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# ✅ Problem:
# Find the minimum ship capacity to deliver all packages within `D` days.
# Packages must be shipped in order and cannot be split.

# 📚 Pattern:
# Binary Search on Answer Space

# 🔍 Key Insight:
# - Min capacity = max(weights) (you must carry the heaviest package)
# - Max capacity = sum(weights) (carry everything in one day)
# - Binary search the min valid capacity that ships all packages within D days

# 🧠 Memory Hook:
# binary search min ship capacity
# left = max(weights), right = sum(weights)
# simulate shipping days: if days > D → capacity too small → move right
# if days ≤ D → try smaller → move left

# ✅ Time Complexity: O(n log(sum - max))
# - binary search the capacity from max(weights) to sum(weights) → log(sum - max) steps
# Each step runs a greedy check over all weights → O(n) time
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Start binary search from max(weights), not 0
# - Use strict bounds: if days_used > D → invalid capacity
# - Must ship in **order**

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # kept thinking of roundrobin, but using binary search to find the capacity makes sense 
        def canShip(capacity):
            days_used = 1
            curr_weight = 0

            for w in weights:
                if curr_weight + w > capacity: 
                    days_used += 1  # Start a new day
                    curr_weight = 0 
                curr_weight += w
            return days_used <= days

        # 📏 Set initial binary search bounds
        left = max(weights)
        right = sum(weights)

        # 🔀 Binary search for minimum valid capacity
        while left < right: 
            mid = (left + right) // 2
            # 🔄 Can we ship with capacity = mid?
            if canShip(mid):
                # can ship -> try smaller capacity
                right = mid 
            else:
                # can't ship -> try bigger
                left = mid + 1 # Try larger capacity
        return left # 🏆 Smallest capacity that works


# 🔄 Dry Run Example:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# left = 10, right = 55
# mid = 32 → canShip = True → try smaller
# mid = 21 → canShip = False → try bigger
# mid = 26 → canShip = True → try smaller...
# Eventually find answer = 15
