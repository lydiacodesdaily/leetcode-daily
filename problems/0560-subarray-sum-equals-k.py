# LeetCode 560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# ✅ Problem:
# Given an array of integers `nums` and an integer `k`,
# return the total number of continuous subarrays whose sum equals to `k`.

# 🧠 Memory Hook:
# prefix sum + hashmap
# sum_i - sum_j = k → if (curr_sum - k) seen before → count++
# map stores prefix_sum → frequency

# 📚 Pattern: Prefix Sum + Hash Map

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

# 📌 Common Gotchas:
# - Include 0 → 1 in prefix sum map to catch subarrays starting from index 0
# - Don’t use sliding window (works only for all positive numbers)

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # base case: empty prefix

        for num in nums:
            curr_sum += num
            if (curr_sum - k) in prefix_sums:
                count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1

        return count

# 🔁 Dry Run Example:
# nums = [1,2,3], k = 3
# prefix_sum = [1,3,6]
# count += 1 when curr_sum = 3 (prefix_sum == k)
# count += 1 again when curr_sum = 6 and (6-3=3) was seen before
# total = 2