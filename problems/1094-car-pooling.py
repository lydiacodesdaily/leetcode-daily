# LeetCode 1094 - Car Pooling
# https://leetcode.com/problems/car-pooling/

# ✅ Problem:
# You're given a list of trips [num_passengers, start_location, end_location].
# Return True if it's possible to carry all passengers without exceeding the car's capacity.

# 🧩 Base Pattern:
# Prefix Sum using a Difference Array
# - Range add: mark pickup and drop-off points
# - Then simulate the ride using prefix sum to get passenger counts

# 🧪 Subtype:
# Timeline Simulation with Count Deltas
# - Efficient way to simulate count updates over a fixed interval (0 to 1000)
# - Works great for capacity tracking and interval overlaps

# 🧠 Memory Hook:
# diff[start] += num, diff[end] -= num
# simulate with prefix sum over locations
# return False if prefix sum > capacity

# ✅ Time Complexity: O(n + 1001) → O(n) for trips, O(1) for locations
# ✅ Space Complexity: O(1001) → constant size array

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 📦 Step 1: Initialize difference array
        diff = [0] * 1001  # index = location, range is 0 to 1000

        # 🚐 Step 2: Apply all trip deltas
        for passengers, start, end in trips:
            diff[start] += passengers    # passengers get in at 'start'
            diff[end] -= passengers      # passengers get out before 'end'

        # 🚦 Step 3: Simulate the timeline
        curr_passengers = 0
        for loc in range(1001):
            curr_passengers += diff[loc]
            if curr_passengers > capacity:
                return False

        return True

# 🔄 Dry Run:
# trips = [[2,1,5], [3,3,7]], capacity = 4
# diff = [0]*1001
# After processing:
# diff[1] += 2 → diff[1] = 2
# diff[5] -= 2 → diff[5] = -2
# diff[3] += 3 → diff[3] = 3
# diff[7] -= 3 → diff[7] = -3
#
# Simulate:
# loc 0: 0
# loc 1: 2
# loc 2: 2
# loc 3: 2+3 = 5 → ❌ exceeds capacity = 4 → return False ✅
