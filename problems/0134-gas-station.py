# LeetCode 134 - Gas Station
# https://leetcode.com/problems/gas-station/
#
# ✅ Problem:
# Given two int arrays gas and cost (length n) around a circular route,
# return the starting station index from which you can complete the circuit once,
# or -1 if impossible.
#
# 📚 Pattern:
# Greedy (single pass) — running balance + restart rule
#
# 🔍 Core Idea:
# diff[i] = gas[i] - cost[i]
# - If total sum(diff) < 0 → impossible no matter where you start.
# - Scan once keeping a local running tank. If tank < 0 at i, then NO index in
#   [start..i] can be a valid start → set start = i+1 and reset tank = 0.
# - If total >= 0, the final 'start' is the unique answer.
#
# 🧠 Memory Hook:
# total >= 0? else -1
# tank += diff; tank < 0 → start = i+1; tank = 0
# return start
#
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)
#
# 📌 Common Gotchas:
# - Forgetting the overall feasibility check (total). You may pick a start that
#   "survives locally" but the route is globally impossible.
# - Not resetting tank to 0 after moving start.
# - Off-by-one when setting start = i + 1.
# - This is GREEDY, not DP.
#
# 🔄 Dry Run (quick):
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# diff = [-2,-2,-2,3,3]; total = 0 → possible
# i=0: tank=-2<0 → start=1, tank=0
# i=1: tank=-2<0 → start=2, tank=0
# i=2: tank=-2<0 → start=3, tank=0
# i=3: tank=+3
# i=4: tank=+6 → end → start=3 ✅
#
# 🧩 Why restart works (intuition):
# If tank becomes negative at i, any start in [start..i] reaches i with
# <= that same tank (or worse), so none can finish. The only hope is i+1.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0   # overall feasibility: sum of (gas - cost)
        tank = 0    # local running tank for current candidate start
        start = 0   # current candidate starting index

        # Single merged pass: compute total & apply greedy restart rule
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            # If current segment fails here, no start in [start..i] can be valid.
            if tank < 0:
                start = i + 1
                tank = 0

        # If overall gas is insufficient, impossible; otherwise 'start' is the answer.
        return start if total >= 0 else -1


# --- Embedded Example ---
# Input:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# Expected Output: 3
#
# Explanation:
# Starting at index 3: tank progression
# i=3: +4-1=+3 → tank=3
# i=4: +5-2=+3 → tank=6
# i=0: +1-3=-2 → tank=4
# i=1: +2-4=-2 → tank=2
# i=2: +3-5=-2 → tank=0 → complete circuit ✅