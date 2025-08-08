# LeetCode 503 - Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

# ✅ Problem:
# Given a circular array nums, for each index i return the first element to the right
# (wrapping around) that is greater than nums[i]. If none exists, return -1 at that index.

# 📚 Pattern:
# Monotonic (decreasing) stack over indices + simulate circularity by iterating 2n.

# 🔍 Key Insight:
# - Use a stack of **indices** (values can repeat).
# - Traverse i in [0 .. 2n-1], let cur = nums[i % n].
# - While stack not empty and nums[stack[-1]] < cur:
#       res[stack.pop()] = cur
# - Push i (only when i < n) so each index appears once.
# - Initialize res with -1 to cover "no greater" by default.

# 🧠 Memory Hook:
# "Indices stack, iterate 2n, fill res on pops"
# (values may repeat ⇒ can't map value→answer; use index→answer)

# ✅ Time Complexity: O(n) — each index pushed/popped at most once
# ✅ Space Complexity: O(n) — stack + result

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n              # store next greater for each index
        stack = []                  # decreasing stack of indices (nums[idx] decreasing)

        # Iterate twice to simulate circular array
        for i in range(2 * n):
            cur = nums[i % n]
            # Resolve any indices whose next greater is 'cur'
            while stack and nums[stack[-1]] < cur:
                idx = stack.pop()
                res[idx] = cur
            # Only push indices from the first pass
            if i < n:
                stack.append(i)

        return res

# 🔄 Dry Run (conceptual)
# nums = [1, 2, 1], n=3
# i=0 (cur=1): stack=[0]
# i=1 (cur=2): pop 0 -> res[0]=2; stack=[]; push 1 -> stack=[1]
# i=2 (cur=1): 1 < nums[1]=2? no -> push 2 -> stack=[1,2]
# i=3 (cur=1): 1 >? nums[2]=1 no; nums[1]=2 no
# i=4 (cur=2): pop 2 -> res[2]=2; stack=[1] (2 !> 2) stop
# i=5 (cur=1): nothing pops
# End: res = [2, -1, 2]

# 📌 Gotchas:
# - Push indices (not values) because values can repeat.
# - Only push indices during the first pass (i < n) to avoid duplicates.
# - Pre-fill res with -1 so "no greater" cases are already handled.