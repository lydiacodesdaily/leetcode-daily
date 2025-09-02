# LeetCode 75 - Sort Colors
# https://leetcode.com/problems/sort-colors/

# ✅ Problem:
# Given an array nums with n objects colored red (0), white (1), or blue (2),
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red → white → blue.

# 📚 Pattern:
# Counting Sort (In-Place)

# 🔍 Key Insight:
# - Count how many of each color (0, 1, 2)
# - Overwrite the nums list in-place based on counts

# 🧠 Memory Hook:
# count colors → overwrite nums in-place

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) extra (uses only constant extra space)

from typing import List
import collections

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = collections.Counter(nums)

        i = 0
        for color in [0, 1, 2]:
            for _ in range(count[color]):
                nums[i] = color
                i += 1


# 🔄 Dry Run Example:
# Input: [2, 0, 2, 1, 1, 0]
# Count: {0:2, 1:2, 2:2}
# Output: [0, 0, 1, 1, 2, 2]

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]

#### PREFERRED VERSION ####
# LeetCode 75 - Sort Colors
# https://leetcode.com/problems/sort-colors/

# ✅ Problem:
# Given an array nums with n objects colored red (0), white (1), or blue (2),
# sort them in-place so that objects of the same color are adjacent, in the order 0s, then 1s, then 2s.

# 📚 Pattern:
# Dutch National Flag (three-way partition)

# 🔍 Core Idea:
# Maintain three regions with pointers:
#   [0..low-1]    → all 0s
#   [low..i-1]    → all 1s (processed middle)
#   [high+1..n-1] → all 2s
# Traverse with `i`, and:
#   - If nums[i] == 0: swap to `low`, expand 0s zone, advance both `low` and `i`
#   - If nums[i] == 1: it's in the middle zone → just i += 1
#   - If nums[i] == 2: swap to `high`, shrink 2s zone, DO NOT increment i (re-check swapped-in value)

# 🧠 Memory Hook:
# three zones: [0s] [1s] [2s]
# 0 → swap with low, ++low, ++i
# 1 → just ++i
# 2 → swap with high, --high, (no i++)

# ✅ Time Complexity: O(n) — single pass
# ✅ Space Complexity: O(1) — in-place

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag algorithm
        low, i, high = 0, 0, len(nums) - 1

        # Invariants:
        # nums[0..low-1]   == 0
        # nums[low..i-1]   == 1
        # nums[high+1..end]== 2
        # nums[i..high]    == unknown
        while i <= high:
            # three zones: [0s] [1s] [2s]
            if nums[i] == 0:
                # 0 ↔ swap with low, ++low, ++i
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] == 1:
                # 1 ↔ just ++i
                # 1 is already in the middle partition 
                i += 1
            else: # nums[i] == 2 
                # 2 ↔ swap with high, –high, (no i++)
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1 
                # NOTE: Do NOT increment i here (need to re-check swapped value)

# -------------------------------
# 🔄 Dry Run
# Input: [2,0,2,1,1,0]
# low=0, i=0, high=5
# i=0: nums[i]=2 → swap(i,high) → [0,0,2,1,1,2], high=4, i=0 (recheck)
# i=0: nums[i]=0 → swap(i,low)  → [0,0,2,1,1,2], low=1, i=1
# i=1: nums[i]=0 → swap(i,low)  → [0,0,2,1,1,2], low=2, i=2
# i=2: nums[i]=2 → swap(i,high) → [0,0,1,1,2,2], high=3, i=2 (recheck)
# i=2: nums[i]=1 → i=3
# i=3: nums[i]=1 → i=4 (stop since i>high)
# Result: [0,0,1,1,2,2] ✅
# -------------------------------
