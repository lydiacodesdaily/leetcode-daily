# LeetCode 15 - 3Sum
# https://leetcode.com/problems/3sum/

# ✅ Problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.

# 📚 Pattern:
# Two Pointers (after sorting)
# - Fix one number, then solve 2-sum with two pointers (left/right).

# 🔍 Key Insight:
# - Sort nums first.
# - For each fixed i:
#   - Skip duplicate nums[i].
#   - Use twoSumII (left, right pointers) to find valid pairs.
# - Skip duplicates on left pointer after finding a triplet.

# 🧠 Memory Hook:
# - sort → fix i → two-pointer
# - skip duplicates: i (nums[i-1]) and left (nums[left-1])
# - stop early if nums[i] > 0

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(n) for output (extra O(1) working space)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix one, move left, right
        res = [] 
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:       # since sorted, no further triplets possible
                break
            if i == 0 or nums[i] != nums[i - 1]:   # skip duplicate fixed values
                self.twoSumII(nums, i, res)
        return res 

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                # found a valid triplet
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


# 🔄 Dry Run:
# Input: nums = [-1,0,1,2,-1,-4]
# Sorted: [-4,-1,-1,0,1,2]
# i=0 → -4 → twoSumII → no triplets
# i=1 → -1 → twoSumII finds [-1,-1,2] and [-1,0,1]
# i=2 → -1 (dup, skipped)
# i=3 → 0 → twoSumII → no new triplets
# Result: [[-1,-1,2], [-1,0,1]]