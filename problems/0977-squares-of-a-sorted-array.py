# LeetCode 977 - Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

# ✅ Problem:
# Given a sorted array of integers (may contain negatives),
# return a new array of the squares of each number, **also sorted in non-decreasing order**.

# 📚 Pattern: Two Pointers
# - Array is already sorted, but squaring may mess up the order (e.g., negative numbers become positive).
# - So we compare absolute values from both ends and fill the result **from the end to start**.

# 🧠 Memory Hook:
# two pointers → fill from end
# left^2 vs right^2 → insert larger to res[pos]
# move pointer of larger one inward

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # result array

        left, right = 0, n - 1
        pos = n - 1  # fill from back

        # 🧭 Process each number from back to front
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return res

# 🔄 Dry Run:
# Input: nums = [-4, -1, 0, 3, 10]
# Square values: [16, 1, 0, 9, 100]
# Output:       [0, 1, 9, 16, 100]