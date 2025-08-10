# LeetCode 55 - Jump Game
# https://leetcode.com/problems/jump-game/
#
# ✅ Problem:
# Given an array nums where nums[i] is the maximum jump length from index i,
# return True if you can reach the last index; otherwise, False.
#
# 📚 Pattern:
# Greedy — track the farthest reachable index as you scan left→right
#
# 🔍 Core Idea:
# Maintain max_reach = farthest index reachable so far.
# For each index i:
#   - If i > max_reach: you can't even land on i → stuck → return False
#   - Otherwise update: max_reach = max(max_reach, i + nums[i])
#   - Early exit if max_reach >= last index
#
# 🧠 Memory Hook:
# max_reach = farthest seen
# if i > max_reach → stuck → False
# max_reach = max(max_reach, i + nums[i])
# if max_reach ≥ last → True
#
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)
#
# 📌 Common Gotchas:
# - You may jump LESS than nums[i] (not exactly nums[i]).
# - Reaching or going PAST the last index counts as success.
# - Don't simulate specific jumps; just keep farthest reach.
#
# 🔄 Dry Runs:
# 1) nums = [2,3,1,1,4]
#    i=0: max_reach=max(0,0+2)=2
#    i=1: 1<=2 → max_reach=max(2,1+3)=4 → 4>=last(4) → True ✅
#
# 2) nums = [3,2,1,0,4]
#    i=0: max_reach=3
#    i=1: max_reach=max(3,3)=3
#    i=2: max_reach=max(3,3)=3
#    i=3: max_reach=max(3,3)=3
#    i=4: i(4)>max_reach(3) → False ❌ (stuck at 3)
#
# 3) nums = [2,0]
#    i=0: max_reach=max(0,0+2)=2 → 2>=last(1) → True ✅
#    (You can jump ≤2 steps; jumping 2 passes the last index → success)
#
# --- Clean interview implementation with grouped skeletal steps ---

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n - 1
        max_reach = 0  # farthest index we can reach so far

        # 🧭 Single pass: expand the reachable frontier
        for i, jump in enumerate(nums):
            # If current index is beyond our reachable frontier, we're stuck
            if i > max_reach:
                return False

            # Expand the frontier from here
            max_reach = max(max_reach, i + jump)

            # Early success if we can already reach or pass the last index
            if max_reach >= last:
                return True

        # If we never got stuck through the whole array, we're good
        return True


# --- Embedded Examples ---
# Example A:
# nums = [2,3,1,1,4] → True
# Example B:
# nums = [3,2,1,0,4] → False
# Example C:
# nums = [2,0]       → True