# LeetCode 18 - 4Sum
# https://leetcode.com/problems/4sum/

# ✅ Pattern:
# Sort + Two Pointers inside nested loops (i, j, left, right)

# 🧠 Memory Hook:
# Fix i + j → search left/right
# Skip duplicates for all 4 pointers
# Return List[List[int]]

# ✅ Time: O(n^3)
# ✅ Space: O(1) extra (excluding result)

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

"""
🔄 Dry Run Example:
Input: nums = [1,0,-1,0,-2,2], target = 0
Sorted: [-2, -1, 0, 0, 1, 2]
Output: [
  [-2, -1, 1, 2],
  [-2,  0, 0, 2],
  [-1,  0, 0, 1]
]
"""