# LeetCode 31 - Next Permutation
# https://leetcode.com/problems/next-permutation/

# ✅ Problem:
# Rearrange the list into the next lexicographical permutation.
# If not possible, rearrange it as the lowest possible order (sorted ascending).

# 🔍 Key Insight:
# Traverse the array from the end:
# - Find the first decreasing element
# - Swap it with the next greater number to the right
# - Reverse the suffix

# 🔁 Key Observations:
# - We only need to make the smallest change that gives a bigger permutation.
# - If no such change is possible, reverse the entire array.

# 📚 Pattern: Array Manipulation / Two Pointers

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) — in-place

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Example dry run: nums = [1, 3, 2]
        # Goal: Get the next lexicographical permutation
        # Expected Output: [2, 1, 3]

        n = len(nums)
        i = n - 2  # Start from second last index

        # Step 1️⃣: Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # i = 1 → nums[1] = 3 >= 2 → i = 0
        # i = 0 → nums[0] = 1 < 3 → stop

        if i >= 0:
            # Step 2️⃣: Find the number just larger than nums[i] to the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # j = 2 → nums[2] = 2 > 1 → valid

            # Step 3️⃣: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # nums = [2, 3, 1]

        # Step 4️⃣: Reverse the suffix (i+1 to end)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # Reverse [3, 1] → [1, 3]
        # Final result: [2, 1, 3]

# 🧠 Summary:
# - Step 1: Find pivot (first drop from right)
# - Step 2: Swap with just-larger number on right
# - Step 3: Reverse everything to the right of pivot
# This gives the next smallest lexicographical arrangement.

# 📌 Common Gotchas:
# - Forgetting to reverse the suffix after the swap
# - Handling the case when the entire array is in descending order