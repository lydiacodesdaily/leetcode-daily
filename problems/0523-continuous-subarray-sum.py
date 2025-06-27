# LeetCode 523 - Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# ✅ Problem:
# Given an integer array nums and an integer k, return true if nums has
# a continuous subarray of size at least two whose elements sum up to a multiple of k.

# 📚 Pattern:
# Prefix Sum + Hash Map
# - Track prefix_sum % k remainders
# - If the same remainder appears again, the subarray sum between them is divisible by k

# 🔍 Core Idea:
# Use prefix sum modulo k to track remainders.
# If two prefix sums have the same remainder → the subarray sum between them is divisible by k.
# Store the earliest index for each remainder.
# When the same remainder appears again, check if the subarray length is at least 2.

# 🧐 Memory Hook:
# prefix_sum % k → store earliest index
# same remainder found again → subarray sum divisible by k
# subarray length = j - i ≥ 2 → check distance before return

# Core Knowledge:
# - prefix_sum[i] is the sum from index 0 to index i.
# - prefix_sum[j] is the sum from index 0 to index j (j > i).
# => Subarray sum from index i+1 to j = prefix_sum[j] - prefix_sum[i]
# => (prefix_sum[j] - prefix_sum[i]) % k == 0  →  means the subarray sum is divisible by k
# => prefix_sum[j] % k == prefix_sum[i] % k
# If two prefix sums have the same remainder modulo k, the subarray between them is divisible by k.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(min(n, k)) → because remainder map size can be at most k different values

# 📌 Common Gotchas:
# - Must check subarray length ≥ 2 → j - i ≥ 2
# - Handle k = 0 case separately → need exact zero subarray sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Key = prefix_sum % k, Value = earliest index where this remainder appeared
        remainder_index = {0: -1}  # Initialize with remainder 0 at index -1 for edge cases
        prefix_sum = 0

        # 🗽 Iterate through the array
        for i, num in enumerate(nums):
            prefix_sum += num

            # 🛢️ If k != 0, take modulo to get remainder
            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum  # Special handling when k == 0 → looking for exact sum == 0

            # 🌟 Check if this remainder was seen before
            if remainder in remainder_index:
                # Check if subarray length is at least 2
                if i - remainder_index[remainder] >= 2:
                    return True  # Found a valid subarray
            else:
                # 📂 Store the earliest index where this remainder was seen
                remainder_index[remainder] = i

        return False  # No valid subarray found

# 🔄 Dry Run:
# Input: nums = [23, 2, 4, 6, 7], k = 6
# prefix sums: [23, 25, 29, 35, 42]
# remainders: [5, 1, 5, 5, 0]
# At index 2 → remainder 5 seen before at index 0 → subarray length = 2 → return True ✅
