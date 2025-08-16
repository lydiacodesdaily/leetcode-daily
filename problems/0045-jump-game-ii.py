# LeetCode 45 - Jump Game II
# https://leetcode.com/problems/jump-game-ii/
#
# ✅ Problem:
# Given an array nums where nums[i] is the maximum jump length from index i,
# return the minimum number of jumps to reach the last index.
#
# 📚 Pattern:
# Greedy — BFS-by-level over index ranges ("windows")
#
# 🔍 Core Idea:
# - Treat indices as layers of reachability within the same jump.
# - Maintain a "current window" [*, current_end] representing all indices
#   reachable with the current number of jumps.
# - While scanning indices in the current window, keep track of `farthest`
#   (the farthest index we can reach from any index in this window).
# - When i == current_end, we have exhausted the current window → we must take
#   one jump, and the next window becomes up to `farthest`.
#
# 🧠 Memory Hook:
# - count jump when: i == current_end
# - track farthest within window
# - then: current_end = farthest; jumps += 1
# - loop to n-2 only (no jump needed at last index)
#
# ⏱️ Time Complexity: O(n)
# 💾 Space Complexity: O(1)
#
# ⚠️ Common Gotchas:
# - ❌ Don't increment on every time you see a bigger reach — only when you finish the window.
# - ❌ Don't loop to n-1; process up to n-2 because you don't need to jump from the last index.
# - ✅ Initialize: jumps=0, current_end=0, farthest=0.
#
# ---------------------------------------------------------------
# 🧭 Skeleton (grouped steps)
# 1) Handle trivial case (n <= 1) → 0 jumps
# 2) Initialize jumps, current_end, farthest
# 3) For i in [0..n-2]:
#      - farthest = max(farthest, i + nums[i])
#      - if i == current_end: close window → jumps += 1; current_end = farthest
#        * early break if current_end >= n-1
# 4) return jumps
# ---------------------------------------------------------------

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy window expansion (BFS by layers over indices).

        While iterating, we maintain:
        - farthest: farthest place we can reach in the current jump window
        - current_end: the end index of the current jump window
        We count a jump only when we finish scanning the current window (i == current_end).
        """
        n = len(nums)
        if n <= 1:
            return 0  # already at or beyond the last index

        jumps = 0
        current_end = 0
        farthest = 0

        # Process up to n-2; once our window reaches the last index, we're done.
        for i in range(n - 1):
            # Best reach we can extend to using index i
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of the current window,
            # we must take a jump and expand the window.
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit: if our window now reaches/passes the last index
                if current_end >= n - 1:
                    break

        return jumps

# ---------------------------------------------------------------
# 🔄 Dry Run (Example)
# nums = [2, 3, 1, 1, 4]
# n=5
# jumps=0, current_end=0, farthest=0
# i=0: farthest = max(0, 0+2)=2; i==current_end → jumps=1, current_end=2
# i=1: farthest = max(2, 1+3)=4
# i=2: farthest = max(4, 2+1)=4; i==current_end → jumps=2, current_end=4 (≥ n-1) → break
# return 2
#
# Another sanity check:
# nums = [2,1,1,1,1]
# - Optimal path: 0 → 2 → 4 → 2 jumps
# Our algorithm:
# i=0: farthest=2; i==current_end → jumps=1, current_end=2
# i=1: farthest=max(2, 1+1)=2
# i=2: farthest=max(2, 2+1)=3; i==current_end → jumps=2, current_end=3
# i=3: farthest=max(3, 3+1)=4 → early exit on next window expansion (≥ last)
# ---------------------------------------------------------------
#
# 🧪 Quick Usage:
# s = Solution()
# print(s.jump([2,3,1,1,4]))  # -> 2
# print(s.jump([2,1,1,1,1]))  # -> 2