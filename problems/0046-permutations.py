# LeetCode 46 - Permutations
# https://leetcode.com/problems/permutations/
#
# ✅ Problem:
# Given an array nums of distinct integers, return all possible permutations.
#
# 📚 Pattern:
# Backtracking (DFS) with path-building
#
# 🔍 Core Idea:
# - Build permutations incrementally in a `curr` list.
# - At each step, try adding an unused element.
# - When `curr` has length == n, record it as a complete permutation.
#
# 🧠 Memory Hook:
# - choose num not yet in curr
# - recurse
# - undo (pop)
#
# ⏱️ Time Complexity: O(n · n!)   (n! permutations × O(n) to copy list)
# 💾 Space Complexity: O(n)        (recursion stack + current path)
#
# ⚠️ Common Gotchas:
# - Must copy `curr[:]` instead of appending reference
# - Using `if num not in curr` → O(n) check; fine for interviews but can be optimized with a `used` set/array.
# - Works only with distinct elements (as guaranteed here).
#
# ---------------------------------------------------------------
# 🧭 Skeletal Steps
# 1) Define backtrack(curr):
#      - If len(curr) == len(nums): add a copy to ans
#      - Else, loop each num in nums:
#            if num not in curr:
#                append num
#                recurse
#                pop (backtrack)
# 2) Call backtrack([]) and return ans
# ---------------------------------------------------------------

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking by path-building.
        At each call, extend `curr` with an unused num,
        recurse, then undo the choice.
        """
        def backtrack(curr: List[int]) -> None:
            # Base case: built a complete permutation
            if len(curr) == len(nums):
                ans.append(curr[:])  # must append a copy
                return 

            # Try each num not yet used
            for num in nums:
                if num not in curr:          # O(n) lookup
                    curr.append(num)        # choose
                    backtrack(curr)         # explore
                    curr.pop()              # un-choose (backtrack)

        ans: List[List[int]] = []
        backtrack([])
        return ans

# ---------------------------------------------------------------
# 🔄 Dry Run (Example)
# nums = [1,2,3]
# backtrack([]):
#   try 1 -> curr=[1]
#     try 2 -> curr=[1,2]
#       try 3 -> curr=[1,2,3] → complete → append [1,2,3]
#     backtrack, curr=[1]
#     try 3 -> curr=[1,3]
#       try 2 -> curr=[1,3,2] → complete → append [1,3,2]
#   backtrack, curr=[]
#   try 2 -> ...
#   try 3 -> ...
# Output:
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# ---------------------------------------------------------------