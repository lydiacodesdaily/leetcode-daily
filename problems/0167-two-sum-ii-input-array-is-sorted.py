# LeetCode 167 - Two Sum II (Input Array Is Sorted)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# 📚 Pattern:
# Two Pointers — opposite ends moving inward

# 🔍 Core Idea:
# Since array is sorted, use left/right pointers.
# If sum too small → move left up.
# If sum too big → move right down.
# Stop when sum matches target.

# 🧠 Memory Hook:
# sorted → 2ptr  
# sum < target → L++  
# sum > target → R--  
# match → return 1-based indices  

# ✅ Time: O(n)
# ✅ Space: O(1)

# 📌 Common Gotchas:
# - Return **1-based indices**, not 0-based.
# - Use left < right (not ≤), because solution guaranteed.
# - Don’t overthink — no need for hashing since sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # -----------------------------------------
        # 1️⃣ Initialize two pointers
        # -----------------------------------------
        left, right = 0, len(numbers) - 1

        # -----------------------------------------
        # 2️⃣ Move pointers until they meet
        # -----------------------------------------
        while left < right:
            curr_sum = numbers[left] + numbers[right]

            # -------------------------------------
            # 3️⃣ Compare sum with target
            # -------------------------------------
            if curr_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]

            elif curr_sum < target:
                # Too small → need larger sum → move left
                left += 1
            else:
                # Too large → need smaller sum → move right
                right -= 1

        # Should never reach here because problem guarantees a solution
        return []

# 🔄 Dry Run:
# Input:
# numbers = [2,7,11,15], target = 9
#
# left=0 (2), right=1 (7) → sum=9 → match → return [1,2]