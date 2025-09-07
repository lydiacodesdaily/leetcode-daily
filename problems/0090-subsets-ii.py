# LeetCode 90 - Subsets II
# https://leetcode.com/problems/subsets-ii/
#
# ✅ Problem:
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set),
# ensuring no duplicate subsets are included.
#
# 📚 Pattern:
# Backtracking (DFS) with duplicate skipping
#
# 🔍 Core Idea:
# - Sort nums so duplicates are adjacent
# - At each recursion depth:
#     * Always record the current path as a valid subset
#     * Iterate i from start..end
#     * If nums[i] == nums[i-1] and i > start → skip duplicate at this depth
#     * Else, include nums[i] and recurse
#
# 🧠 Memory Hook:
# dfs(start, path)
#   res.append(path[:])
#   for i in range(start..):
#       if i > start and nums[i] == nums[i-1]: continue
#       path.append(nums[i]); dfs(i+1); path.pop()
#
# ✅ Time Complexity: O(n * 2^n) (output bound)
# ✅ Space Complexity: O(n) recursion depth; O(n * 2^n) including output

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # input: nums may contain duplicates
        # output: list of all unique subsets
        res = []
        nums.sort()  # sort so duplicates are adjacent

        def dfs(start: int, path: List[int]) -> None:
            res.append(path[:])  # record current subset

            for i in range(start, len(nums)):
                # skip duplicates at the same depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res


# 🔄 Example
# Input: nums = [1,2,2]
# Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]