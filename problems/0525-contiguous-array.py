# LeetCode 525 - Contiguous Array
# https://leetcode.com/problems/contiguous-array/

# ✅ Problem:
# Given a binary array `nums`, find the length of the longest contiguous subarray 
# that contains an equal number of 0s and 1s.

# 🧩 Pattern:
# Prefix Sum + HashMap (similar to subarray sum = k)

# 🔍 Key Insight:
# - Treat 0 as -1.
# - The problem becomes: Find the longest subarray with sum = 0.
# - Use a hashmap to store the **first index** where each prefix_sum occurs.
# - If prefix_sum is seen again → subarray between previous and current index sums to 0.

# 🧠 Memory Hook:
# - 0 → -1
# - hashmap of {prefix_sum: first_index}
# - repeat prefix_sum → subarray sum = 0 → update max_len

# ✅ Time: O(n)
# ✅ Space: O(n)

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        first_seen = {0: -1}  # Map prefix_sum to earliest index
        max_len = 0

        for i, num in enumerate(nums):
            # Replace 0 with -1 to make prefix sum logic work
            prefix_sum += -1 if num == 0 else 1

            if prefix_sum in first_seen:
                length = i - first_seen[prefix_sum]
                max_len = max(max_len, length)
            else:
                first_seen[prefix_sum] = i

        return max_len

# 📌 Example Dry Run:
# nums = [0, 1, 0]
# Step-by-step:
# i=0 → num=0 → sum=-1 → store {-1:0}
# i=1 → num=1 → sum=0 → seen at -1 → length = 2 → max_len = 2
# i=2 → num=0 → sum=-1 → seen at 0 → length = 2 → max_len = 2
# ✅ Output: 2
