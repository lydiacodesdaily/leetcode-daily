# LeetCode 560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# ✅ Problem:
# Given an integer array nums and an integer k,
# return the total number of **contiguous subarrays** that sum to k.

# 🔍 Key Insight:
# Use a **prefix sum** + hashmap:
# - Keep track of running sum `curr_sum`
# - At each index, check if (curr_sum - k) has been seen before
#   → It means there exists a subarray that sums to k

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # To count subarrays that start from index 0

        for num in nums:
            curr_sum += num
            count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1

        return count

"""
Dry-Run:

nums = [1, 1, 1], k = 2

Step 1: curr_sum = 1 → curr_sum - k = -1 → not in map
Step 2: curr_sum = 2 → curr_sum - k = 0 → found 1 → count = 1
Step 3: curr_sum = 3 → curr_sum - k = 1 → found 1 → count = 2 ✅
"""