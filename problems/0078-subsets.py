# LeetCode 78 - Subsets
# https://leetcode.com/problems/subsets/

# ✅ Problem:
# Given an integer array `nums` of unique elements, return *all possible subsets* (the power set).
# The solution set must not contain duplicate subsets.

# 📚 Pattern:
# Backtracking (DFS with include/exclude branching)

# 🔍 Key Insight:
# - Each element has 2 choices → include or exclude
# - Use DFS to recursively build subsets along both paths

# 🧠 Memory Hook:
# dfs(index, path)
# include: path + [nums[index]]
# exclude: path stays the same
# base case → if index == len(nums): res.append(path[:])

# ✅ Time Complexity: O(n × 2^n)
# - 2^n subsets total
# - up to O(n) to copy each path into result

# ✅ Space Complexity: O(n × 2^n)
# - Recursion stack: O(n)
# - Output list: O(n × 2^n)

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index: int, path: List[int]):
            # 🧭 Base case: all elements considered
            if index == len(nums):
                res.append(path[:])  # append a copy of current subset
                return
            
            # ✅ Option 1: Include nums[index]
            path.append(nums[index])
            dfs(index + 1, path)

            # ⬅️ Backtrack
            path.pop()

            # ✅ Option 2: Exclude nums[index]
            dfs(index + 1, path)

        # 🔁 Start DFS from index 0 with empty path
        dfs(0, [])
        return res

# 🔄 Dry Run:
# Input: nums = [1, 2]
# dfs(0, [])
#   ├─ include 1 → dfs(1, [1])
#   │    ├─ include 2 → dfs(2, [1, 2]) → append
#   │    └─ exclude 2 → dfs(2, [1]) → append
#   └─ exclude 1 → dfs(1, [])
#        ├─ include 2 → dfs(2, [2]) → append
#        └─ exclude 2 → dfs(2, []) → append
# Output: [ [1,2], [1], [2], [] ]