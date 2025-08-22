# LeetCode 560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
#
# ✅ Problem:
# Count the number of continuous subarrays whose sum equals k.
#
# 📚 Pattern: Prefix Sum + Hash Map
#
# 🔍 Core Idea:
# - Let prefix_sum = sum of nums[0..i]
# - We want subarray(l..i) = k
#   → prefix_sum[i] - prefix_sum[l-1] = k
#   → prefix_sum[l-1] = prefix_sum[i] - k
# - So at each index, we check: "how many earlier prefix sums
#   equal (current_prefix - k)?"
# - Each such earlier prefix corresponds to a valid subarray ending here.
#
# 🧠 Memory Hook:
# - need earlier = current_prefix - k
# - answer += freq[current_prefix - k]
# - then freq[current_prefix] += 1
# - seed freq[0] = 1   (empty prefix, allows subarrays starting at index 0)
#
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)
#
# ⚠️ Common Pitfalls:
# - Forgetting to initialize freq[0] = 1
# - Updating freq before using it
# - Thinking one earlier prefix is enough — but multiple equal prefix sums
#   at different indices all count separately (different subarrays)

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # running prefix sum
        prefix_sum = 0
        # total number of valid subarrays
        count_subarrays = 0
        # frequency map of prefix sums seen so far
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1   # empty prefix to handle subarrays starting at index 0

        for num in nums:
            prefix_sum += num

            # check if there are earlier prefixes that make sum = k
            need = prefix_sum - k
            count_subarrays += prefix_freq[need]

            # record this prefix sum
            prefix_freq[prefix_sum] += 1

        return count_subarrays


# 🔄 Dry Run Example
# nums = [1, 2, 3], k = 3
# prefix sums: [1, 3, 6]
#
# i=0 → prefix=1, need=-2 → none → ans=0
# i=1 → prefix=3, need=0 → found 1 → ans=1 ([1,2])
# i=2 → prefix=6, need=3 → found 1 → ans=2 ([3])
# Final answer = 2