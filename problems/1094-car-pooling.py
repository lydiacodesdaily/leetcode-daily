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

# 🔍 Core Idea:
# Use a difference array to track passenger changes at each stop.
# Prefix sum while driving the bus route to track the real-time passenger load.

# 🧠 Memory Hook:
# 🚌 Bus Ride Story:
# + Passengers get on → mark positive at that stop
# - Passengers get off → mark negative at that stop
# 🚗 Drive the bus (prefix sum) → track total passengers at each stop
# 🚨 If overloaded → return False
# ✅ If safe → return True

# 🧠 Memory Hook:
# diff[start] += num, diff[end] -= num
# simulate with prefix sum over locations
# return False if prefix sum > capacity

# ✅ Time Complexity: O(n + 1001) → O(n) for trips, O(1) for locations
# ✅ Space Complexity: O(1001) → constant size array

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 🚌 Imagine we have a passenger flow chart for each bus stop (index 0 ~ 1000)
        stops = [0] * 1001  # Locations 0 ~ 1000 → each index is a bus stop

        for num_passengers, start, end in trips:
            # 🛑 Passengers get ON the bus at 'start' stop → add to flow chart
            stops[start] += num_passengers

            # 🛑 Passengers get OFF the bus at 'end' stop → subtract from flow chart
            stops[end] -= num_passengers

        # 🚗 Drive the bus from stop 0 to stop 1000
        current_passengers = 0
        for stop in range(1001):
            # 🚌 Update the bus load as passengers get on/off
            current_passengers += stops[stop]

            # 🚨 If the bus gets too crowded → return False
            if current_passengers > capacity:
                return False

        # ✅ If we finished the route safely → trip is valid
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
