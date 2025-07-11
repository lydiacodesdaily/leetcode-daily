# LeetCode 75 - Sort Colors
# https://leetcode.com/problems/sort-colors/

# ✅ Problem:
# Given an array nums with n objects colored red (0), white (1), or blue (2),
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red → white → blue.

# 📚 Pattern:
# Counting Sort (In-Place)

# 🔍 Key Insight:
# - Count how many of each color (0, 1, 2)
# - Overwrite the nums list in-place based on counts

# 🧠 Memory Hook:
# count colors → overwrite nums in-place

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) extra (uses only constant extra space)

from typing import List
import collections

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = collections.Counter(nums)

        i = 0
        for color in [0, 1, 2]:
            for _ in range(count[color]):
                nums[i] = color
                i += 1


# 🔄 Dry Run Example:
# Input: [2, 0, 2, 1, 1, 0]
# Count: {0:2, 1:2, 2:2}
# Output: [0, 0, 1, 1, 2, 2]

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]