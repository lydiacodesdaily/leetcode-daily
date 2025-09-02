# LeetCode 523 - Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# ✅ Problem:
# Given an integer array nums and an integer k, return true if nums has a 
# continuous subarray of length at least two whose elements sum up to a 
# multiple of k, or false otherwise.

# 📚 Pattern:
# Prefix Sum + Modulo Hashing
# - If two prefix sums have the same remainder % k, the subarray between them is divisible by k.

# 🔍 Key Insight:
# (prefix[j] - prefix[i]) % k == 0  ⟹  prefix[j] % k == prefix[i] % k
# Use a hashmap to track the *first index* where each remainder is seen.

# 🧠 Memory Hook:
# remainder repeats → subarray divisible by k
# store first index only
# ensure gap ≥ 2 → i - prev_idx > 1

# ✅ Time Complexity: O(n) – one pass
# ✅ Space Complexity: O(k) – hashmap of remainders

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # remainder -> index where it first appeared
        mod_seen = {0: -1}  # seed with remainder 0 at index -1
        prefix_mod = 0

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                # ensure subarray length ≥ 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # store only first occurrence of this remainder
                mod_seen[prefix_mod] = i

        return False


# -------------------------------
# 🔄 Dry Run Examples
# -------------------------------

# Case 1: True
# nums = [23, 2, 4, 6, 7], k = 6
# prefix remainders: [5, 1, 5, 5, 0]
# remainder 5 repeats (index 0 and 2) with gap ≥ 2 → True

# Case 2: False
# nums = [1, 2, 3], k = 5
# prefix remainders: [1, 3, 1]
# remainder 1 repeats (index 0 and 2), but gap = 2 → length=2 → subarray sum=5 ✅ divisible by 5
# Actually → True
# For a False case: nums=[1,2,12], k=7
# prefix remainders: [1,3,1]
# but valid gap never ≥ 2 with divisible sum → False