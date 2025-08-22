# LeetCode 1 - Two Sum
# https://leetcode.com/problems/two-sum/
#
# ✅ Problem:
# Given an array nums and an integer target, return the indices [i, j] (i != j)
# such that nums[i] + nums[j] == target. Assume exactly one solution exists.
#
# 📚 Pattern:
# Hash Map (value -> index), single pass
#
# 🔍 Core Idea:
# As you scan left→right, for each number x = nums[i], check if its complement
# y = target - x has been seen before. If yes, return [index_of_y, i].
# Otherwise store x -> i in a dict for future pairs.
#
# 🧠 Memory Hook:
# "need = target - x; if need in map → answer; else map[x] = i"
#
# ✅ Time Complexity: O(n) — each element looked up/inserted once
# ✅ Space Complexity: O(n) — hash map in worst case
#
# 📌 Common Gotchas:
# - Return **indices**, not values
# - Insert after checking (avoids using the same element twice when target = 2*x)
# - Duplicates are fine; the map keeps the earliest needed index
#
# ————————————————————————————————————————————————————————————————

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # value -> index of first occurrence that matters
        for i, x in enumerate(nums):
            need = target - x
            if need in idx:
                return [idx[need], i]
            idx[x] = i
        # Per problem, a solution always exists. If not, you could raise or return [-1, -1].
        return [-1, -1]

# ————————————————————————————————————————————————————————————————
# 🔄 Dry Run:
# nums = [2, 7, 11, 15], target = 9
# i=0, x=2, need=7, idx={} → not found → idx={2:0}
# i=1, x=7, need=2, idx has 2 at 0 → return [0,1] ✅
#
# Another:
# nums = [3, 3], target = 6
# i=0, x=3, need=3, not found → idx={3:0}
# i=1, x=3, need=3, found at 0 → return [0,1] ✅