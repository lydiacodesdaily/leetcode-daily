# LeetCode 339 - Nested List Weight Sum
# https://leetcode.com/problems/nested-list-weight-sum/

# ✅ Problem:
# Given a nested list of integers, return the sum of all integers in the list 
# weighted by their depth. Each integer is multiplied by the depth at which it's found.

# 🔍 Key Insight:
# Use DFS recursion:
# - If the element is an integer, return value × depth
# - If it's a list, recurse on it with depth + 1

# ✅ Time Complexity: O(n) — each integer is visited once
# ✅ Space Complexity: O(d) — max depth of recursion stack

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nlist, depth):
            total = 0
            for ni in nlist:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        
        return dfs(nestedList, 1)

"""
Input: [1, [4, [6]]]

Depth:
- 1 at depth 1 → 1×1 = 1
- 4 at depth 2 → 4×2 = 8
- 6 at depth 3 → 6×3 = 18

Total = 1 + 8 + 18 = 27 ✅
"""