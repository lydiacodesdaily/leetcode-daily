# LeetCode 53 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# ✅ Problem:
# Given an integer array `nums`, find the contiguous subarray (containing at least one number)
# which has the **largest sum**, and return its sum.

# 📚 Pattern:
# Dynamic Sliding Window (a.k.a. Kadane’s Algorithm)

# 🔍 Key Insight:
# At each index, we decide:
# - Continue the current subarray → curr_sum + nums[i]
# - Or start fresh at nums[i] (if curr_sum is negative)

# 🧠 Memory Hook:
# dynamic window — keep growing if it helps, else reset
# curr_sum = max(nums[i], curr_sum + nums[i])
# max_sum = max(max_sum, curr_sum)

# ✅ Time Complexity: O(n)
# - One pass through the array

# ✅ Space Complexity: O(1)
# - Only tracking two variables: curr_sum and max_sum

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current and max to first element
        curr_sum = max_sum = nums[0]

        # Iterate through remaining elements
        for i in range(1, len(nums)):
            num = nums[i]

            # 🧭 Extend or restart the subarray
            curr_sum = max(num, curr_sum + num)

            # 🥇 Update the global max if needed
            max_sum = max(max_sum, curr_sum)

        return max_sum

# 🔄 Dry Run:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# i=0: curr_sum = -2, max_sum = -2
# i=1: curr_sum = max(1, -2+1) = 1 → max_sum = 1
# i=2: curr_sum = max(-3, 1-3) = -2 → max_sum = 1
# i=3: curr_sum = max(4, -2+4) = 4 → max_sum = 4
# i=4: curr_sum = max(-1, 4-1) = 3 → max_sum = 4
# i=5: curr_sum = max(2, 3+2) = 5 → max_sum = 5
# i=6: curr_sum = max(1, 5+1) = 6 → max_sum = 6
# i=7: curr_sum = max(-5, 6-5) = 1 → max_sum = 6
# i=8: curr_sum = max(4, 1+4) = 5 → max_sum = 6 ✅
#
# Output: 6