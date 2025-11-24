# LeetCode 853 - Car Fleet
# https://leetcode.com/problems/car-fleet/
#
# ✅ Problem:
# There are n cars driving towards a target along a one-lane road.
# - You’re given:
#     - target: the target position (integer)
#     - position[i]: starting position of the i-th car
#     - speed[i]: speed of the i-th car
# Rules:
# - Cars move in the same direction toward "target".
# - A car CANNOT overtake another car.
# - If a faster car reaches a slower car, it must slow down and they form a **fleet**.
# - A fleet moves at the slowest speed among cars in that fleet.
# - Two cars arriving at the target at the **same time** are part of the same fleet.
# Return the **number of car fleets** that will arrive at the target.
#
# 📚 Pattern:
# Sort + Greedy + Monotonic Stack (process from right/closest to target)
#
# 🔍 Core Idea:
# - Instead of simulating movement, compute each car’s **time to reach target**:
#       time[i] = (target - position[i]) / speed[i]
# - Sort cars by position from **closest to farthest from target**.
# - Process them from **right to left** (closest → farthest):
#     - Think of a "stack" of times.
#     - A car behind:
#         - If it would arrive **later or at the same time** → it cannot pass,
#           so it merges into the fleet in front.
#         - If it would arrive **earlier** → it forms a new fleet that never
#           gets caught by anyone ahead.
#
# 🧠 Memory Hook:
# - sort by position ↑
# - compute time = (target - pos) / speed
# - walk from closest → farthest using stack of times
# - if behind_time <= front_time → merge (same fleet)
# - if behind_time > front_time → new fleet++
# - add 1 more for the last remaining stack item → `+ bool(times)`
#
# ✅ Time Complexity: O(n log n)  (sorting cars by position)
# ✅ Space Complexity: O(n)       (storing times / stack)
#
# 📌 Common Gotchas:
# - You must sort by **position**, NOT by speed or time.
# - The processing order is from the car **closest to target** BACKWARDS.
# - When merging fleets, the effective fleet time becomes the **max** (slower) time.
# - `output + bool(times)` is just a shorthand to count the **last fleet** remaining.


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # ---------------------------------------------------------
        # 1️⃣ Pair and sort cars by position (from start → target)
        # ---------------------------------------------------------
        # Each car = (position, speed)
        # After sort: cars[0] is farthest from target, cars[-1] is closest.
        cars = sorted(zip(position, speed))  # O(n log n)

        # ---------------------------------------------------------
        # 2️⃣ Compute time-to-target for each car
        # ---------------------------------------------------------
        # time = (distance to target) / speed
        # Preserve the same ordering as sorted cars.
        times = [float(target - p) / s for p, s in cars]

        # We'll process from right to left (closest to target → farthest)
        fleets = 0

        # ---------------------------------------------------------
        # 3️⃣ Greedy pass from right to left using "stack-like" behavior
        # ---------------------------------------------------------
        # Think:
        # - Pop the "front" (closest to target) car time as the current lead.
        # - Compare with the next car behind it (times[-1]).
        # - If the behind car would arrive later or equal → merges (same fleet).
        # - If the behind car would arrive sooner → separate fleet formed.
        while len(times) > 1:
            lead = times.pop()     # time of the car closest to target (front car)
            behind = times[-1]     # time of the car right behind it

            if lead < behind:
                # Front car arrives earlier → it is NOT caught by the car behind.
                # So this front car *forms its own fleet* that we can finalize.
                fleets += 1
                # We do NOT push lead back because that fleet is done.
            else:
                # lead >= behind:
                # Behind car would arrive earlier or same time…
                # but it *cannot* pass and instead slows down:
                # They form a single fleet that arrives at time = max(lead, behind),
                # which is `lead` here, since lead >= behind.
                #
                # Replace the behind car's time with the fleet's time (lead).
                times[-1] = lead

        # ---------------------------------------------------------
        # 4️⃣ Account for the last remaining fleet (if any)
        # ---------------------------------------------------------
        # At the end of the loop, either:
        # - times is empty  → all fleets already counted.
        # - times has one element → one last fleet not yet counted.
        #
        # bool(times) is:
        # - 1 if times has an element (True)
        # - 0 if times is empty (False)
        return fleets + bool(times)


# 🔄 Example & Dry Run
#
# Example:
#   target = 12
#   position = [10, 8, 3]
#   speed    = [ 2, 4, 3]
#
# Step 1: Pair and sort by position:
#   cars = sorted(zip(position, speed))
#        = sorted([(10,2), (8,4), (3,3)])
#        = [(3,3), (8,4), (10,2)]
#
# Step 2: Compute times:
#   times = [
#       (12 - 3) / 3,    # = 9 / 3 = 3
#       (12 - 8) / 4,    # = 4 / 4 = 1
#       (12 - 10) / 2    # = 2 / 2 = 1
#   ]
#   times = [3, 1, 1]
#
# Step 3: Process from right to left
#   fleets = 0
#
#   Loop 1:
#       lead = times.pop()  → lead = 1, times = [3, 1]
#       behind = times[-1]  → behind = 1
#       lead < behind? 1 < 1 → False
#       So they MERGE:
#           times[-1] = lead = 1
#           times = [3, 1]   (no change in value, but conceptually merged)
#
#   Loop 2:
#       lead = times.pop()  → lead = 1, times = [3]
#       behind = times[-1]  → behind = 3
#       lead < behind? 1 < 3 → True
#       => New fleet formed by this "lead" car
#           fleets += 1  → fleets = 1
#       times = [3]
#
#   Loop ends: len(times) == 1
#
# Step 4: Add last remaining fleet:
#   bool(times) → bool([3]) → True → 1
#   return fleets + bool(times) = 1 + 1 = 2
#
# ✅ Answer: 2 fleets