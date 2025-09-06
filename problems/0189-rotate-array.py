# LeetCode 189 - Rotate Array
# https://leetcode.com/problems/rotate-array/
#
# ✅ Problem:
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# "Rotate to the right by k" means each element moves to (i + k) % n.
# Must be done in-place.
#
# 📚 Pattern:
# Array manipulation → In-place reversal trick (three reversals)
#
# 🔍 Core Idea:
# Right-rotate by k is equivalent to:
#   1) Reverse the whole array
#   2) Reverse the first k elements
#   3) Reverse the remaining n - k elements
#
# 🧠 Memory Hook:
# "right-rotate k → 3 reverses"
# k %= n
# reverse(0, n-1) → reverse(0, k-1) → reverse(k, n-1)
#
# ⏱️ Time: O(n) — each index is reversed at most twice
# 💾 Space: O(1) — in-place
#
# ⚠️ Common Gotchas:
# - Forgetting k %= n (k can be ≥ n)
# - Off-by-one in reverse boundaries
# - Confusing in-place requirement: use nums[:] = ... if you build a new list
#   (nums = new_list only rebinds the local variable and does NOT modify the caller’s list)
#
# 🆚 Alternatives (FYI):
# 1) Extra array: arr[(i + k) % n] = nums[i]; then nums[:] = arr       (O(n) time, O(n) space)
# 2) Cycle replacement (juggling): move elements along cycles           (O(n) time, O(1) space; trickier)
#
# —————————————————————————————————————————————————————————————————————————————

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        In-place 3-reverse method:
          - Normalize k with modulo
          - Reverse the whole array
          - Reverse the first k elements
          - Reverse the remaining n - k elements
        """
        n = len(nums)
        if n <= 1:
            return

        k %= n
        if k == 0:
            return

        # --- helper: reverse nums[l:r] inclusive, in-place
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 1) reverse all
        reverse(0, n - 1)
        # 2) reverse first k
        reverse(0, k - 1)
        # 3) reverse remaining n - k
        reverse(k, n - 1)

# —————————————————————————————————————————————————————————————————————————————
# 🔄 Dry Run:
# nums = [1,2,3,4,5,6,7], k = 3, n = 7
# k %= n → 3
# Step 1: reverse all → [7,6,5,4,3,2,1]
# Step 2: reverse first k=3 → [5,6,7,4,3,2,1]
# Step 3: reverse k..end → [5,6,7,1,2,3,4] ✅
#
# 📝 In-place vs Rebinding:
# If you used the extra-array approach:
#   arr = [0]*n
#   for i in range(n): arr[(i+k)%n] = nums[i]
#   nums[:] = arr   # ✅ updates the original list in-place (caller sees the change)
#   nums = arr      # ❌ only rebinds local 'nums'; caller's list stays unchanged
# —————————————————————————————————————————————————————————————————————————————