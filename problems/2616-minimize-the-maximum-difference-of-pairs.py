# LeetCode 2616 - Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
#
# ✅ Problem:
# You are given an integer array `nums` and an integer `p`.
# Form exactly `p` disjoint pairs (each index used at most once)
# to minimize the maximum difference among the chosen pairs.
# Return the minimum possible value of that maximum difference.
#
# 📚 Pattern:
# Binary Search on Answer + Greedy Feasibility Check
#
# 🔍 Key Insight:
# - Sort first. If we fix a candidate maximum difference (mid),
#   we can greedily form pairs left→right whenever adjacent diff ≤ mid.
# - This greedy works because in sorted order, taking the first available
#   valid pair never blocks a better solution.
# - Since feasibility (“can we form ≥ p pairs?”) is monotone in mid,
#   we binary search for the smallest feasible mid.
#
# 🧠 Memory Hook:
# - sort → guess max diff mid
# - scan greedily: if nums[i+1]-nums[i] ≤ mid → pair, skip both
# - count ≥ p? → shrink mid, else expand
#
# ✅ Time Complexity: O(n log n + n log V) 
#   where V = max(nums) - min(nums)
# ✅ Space Complexity: O(1) extra
#
# 📌 Common Gotchas:
# - Don’t preselect smallest diffs globally—pairs must be disjoint.
# - In greedy scan, advance by 2 if paired, else by 1.
# - Binary search returns the lower bound.

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # T: O(n log V + n log n), S: O(1)
        nums.sort()
        n = len(nums)

        # Greedy feasibility: count how many pairs with diff ≤ mid
        def countValidPairs(mid: int) -> int:
            i = count = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 1   # skip both since paired
                i += 1
            return count

        # Binary search for minimum feasible max diff - find lower bound 
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left

# 🔄 Dry Run Example:
# nums = [10,1,2,7,1,3], p = 2
# sort → [1,1,2,3,7,10]
# left=0, right=9
# mid=4 → pairs (1,1), (2,3) → count=2 ≥ p → feasible
# mid=2 → pairs (1,1) only → count=1 < p → not feasible
# Answer = 3 (smallest feasible max diff)