# LeetCode 1004 - Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

# ✅ Problem:
# Return the maximum number of consecutive 1s in the array
# if you can flip at most `k` 0s to 1s.

# 📚 Pattern: Sliding Window (dynamic size)

# 🧠 Memory Hook:
# sliding window → allow at most k zeros
# if window has > k zeros → shrink from left
# track max window size with valid flips

# 🔍 Key Insight:
# Use a sliding window to maintain a valid subarray that has at most `k` zeros.
# Shrink the window from the left when the count of zeros exceeds `k`.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

# 🔁 Dry Run Example:
# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Window shrinks when more than 2 zeros are in it.
# Final window: [0,0,1,1,1,1,1,1] → length = 6

# 📌 Common Gotchas:
# - Remember to **count zeros**
# - Shrink window as soon as `zero_count > k`, not after
# - Return the **length** of the window each time it's valid

# 🧠 Concepts Reinforced:
# - Sliding window technique to maintain a dynamic subarray
# - Careful tracking of constraints (`k` flips allowed)