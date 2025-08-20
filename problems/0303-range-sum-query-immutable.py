# LeetCode 303 - Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/
#
# ✅ Problem:
# Given an integer array nums, implement the NumArray class:
# - NumArray(int[] nums) initializes the object with nums
# - int sumRange(int left, int right) returns the sum of nums[left...right] inclusive
#
# 📚 Pattern:
# Prefix Sum
#
# 🔍 Core Idea:
# Precompute cumulative sums so each query can be answered in O(1).
#
# 🧠 Memory Hook:
# - prefix[0] = 0
# - prefix[i] = sum(nums[:i])
# - query(l, r) = prefix[r+1] - prefix[l]
#
# ✅ Time Complexity:
# - Build: O(n)
# - Query: O(1)
#
# ✅ Space Complexity: O(n) for prefix array
#
# 📌 Common Gotchas:
# - If you don't use n+1 prefix length, you'll need an if-check for left=0
# - Forgetting to shift right index by +1 when computing prefix

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # prefix[i] = sum(nums[:i]); prefix[0] = 0
        self.prefix = [0]
        running = 0
        for x in nums:
            running += x
            self.prefix.append(running)

    def sumRange(self, left: int, right: int) -> int:
        # sum of nums[left:right+1] = prefix[r+1] - prefix[l]
        return self.prefix[right + 1] - self.prefix[left]

# 🔄 Dry Run Example:
# nums = [-2, 0, 3, -5, 2, -1]
# prefix = [0, -2, -2, 1, -4, -2, -3]
#
# sumRange(0,2) = prefix[3] - prefix[0] = 1 - 0 = 1 ✅
# sumRange(2,5) = prefix[6] - prefix[2] = -3 - (-2) = -1 ✅
# sumRange(0,5) = prefix[6] - prefix[0] = -3 - 0 = -3 ✅
#
# This avoids conditionals with a clean prefix[n+1] style.