# LeetCode 523 - Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# ✅ Problem:
# Given an integer array nums and an integer k, return true if nums has a 
# continuous subarray of at least two elements whose sum is a multiple of k.
# i.e., sum[i:j+1] % k == 0 for some i < j.

# 📚 Pattern: Prefix Sum + HashMap (modulo trick)
# 🔧 Subtype: Match prefix mod seen before → same mod means diff is divisible by k

# 🔍 Key Insight:
# If sum(i...j) % k == 0 → then prefix[j] % k == prefix[i-1] % k
# Track prefix % k in a hashmap with earliest index seen.

# 🧠 Memory Hook:
# prefix sum mod k
# if same mod seen at earlier index i → sum[i+1 to j] % k == 0
# must be len ≥ 2 → check j - i ≥ 2

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(k) at most — only tracking prefix % k in map

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0: -1}  # prefix mod → earliest index

        for i, num in enumerate(nums):
            prefix += num
            mod = prefix % k if k != 0 else prefix  # handle k=0 edge case

            if mod in seen:
                if i - seen[mod] >= 2:
                    return True
            else:
                seen[mod] = i  # only store the earliest index

        return False

# 🔄 Dry Run:
# Input: nums = [23, 2, 4, 6, 7], k = 6
# prefix[0] = 23 → 23 % 6 = 5 → store {5: 0}
# prefix[1] = 25 → 25 % 6 = 1 → store {5:0, 1:1}
# prefix[2] = 29 → 29 % 6 = 5 → 5 seen at index 0 → i - 0 = 2 ✅

# 📌 Gotchas:
# - Must ensure subarray length ≥ 2 → check i - seen[mod] >= 2
# - Don't overwrite mod's earliest index
# - k can be 0 → special case, use raw prefix