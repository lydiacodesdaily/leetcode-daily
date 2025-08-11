# LeetCode 1838 - Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
#
# ✅ Problem:
# Given an integer array nums and an integer k:
#   You can increment any element by 1 up to k times total.
#   Find the maximum frequency of any element after these operations.
#
# 📚 Pattern:
# Sorting + Sliding Window
#
# 🔍 Core Idea:
# - Sort nums ascending.
# - Use a sliding window [left..right]:
#     We want to make all elements in the window equal to nums[right].
# - The cost to do that:
#     cost = nums[right] * window_size - sum(window)
# - If cost > k → shrink window from left.
# - Track max window size seen where cost <= k.
#
# 🧠 Memory Hook:
# sort → target is nums[right]
# cost = target * size - sum_window
# shrink when cost > k
#
# ✅ Time Complexity: O(n log n) — sorting dominates
# ✅ Space Complexity: O(1) extra (O(n) if counting prefix sums explicitly)
#
# 📌 Common Gotchas:
# - Forget to sort first (window logic depends on non-decreasing order)
# - Miscalculate cost without subtracting sum(window)
# - Forget that k is total increments allowed, not per element

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        res = 1

        for right in range(len(nums)):
            total += nums[right] # add actual existing vals

            # Cost to make all in [left..right] = nums[right] * size - total
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1) 
            # feasible #s; will shrink by above if cost > k;

        return res


# 🔄 Dry Run:
# nums = [1,2,4], k = 5
# Sorted: [1,2,4]
#
# right=0: total=1, cost=0 → res=1
# right=1: total=3, cost= 2*2 - 3 = 1 ≤ 5 → res=2
# right=2: total=7, cost= 4*3 - 7 = 5 ≤ 5 → res=3
# ✅ Output=3
#
# Explanation: Increment [1,2,4] → [4,4,4] using 5 increments.

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxFrequency([1,2,4], 5) == 3
    assert sol.maxFrequency([1,4,8,13], 5) == 2
    assert sol.maxFrequency([3,9,6], 2) == 1
    print("All tests passed!")