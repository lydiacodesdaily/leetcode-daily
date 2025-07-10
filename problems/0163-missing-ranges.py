# LeetCode 163 - Missing Ranges
# https://leetcode.com/problems/missing-ranges/

# ✅ Problem:
# Given a sorted array nums of unique integers and a range [lower, upper],
# return a list of the missing ranges within that range (inclusive) 
# that are not present in nums.

# 📚 Pattern:
# Two Pointers / Gap Detection

# 🔍 Key Insight:
# - Add sentinel bounds (lower-1, upper+1) to simplify edge case handling.
# - Traverse adjacent pairs and detect gaps.
# - If there's a gap > 1, the missing range is from (prev+1) to (curr-1)

# 🧠 Memory Hook:
# nums = [lower-1] + nums + [upper+1]
# if gap > 1 → add [prev+1, curr-1]

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []

        # Add sentinel values for simplified edge handling
        nums = [lower - 1] + nums + [upper + 1]

        # Loop through pairs and collect missing ranges
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]
            if curr - prev > 1:
                res.append([prev + 1, curr - 1])

        return res


# 🔄 Example Dry Run:
# Input: nums = [1000000000], lower = 0, upper = 1000000000
# nums = [-1, 1000000000, 1000000001]
# Output: [[0, 999999999]]

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.findMissingRanges([1000000000], 0, 1000000000))  # [[0, 999999999]]
    print(sol.findMissingRanges([2, 4, 7], 1, 10))             # [[1, 1], [3, 3], [5, 6], [8, 10]]
    print(sol.findMissingRanges([], 1, 3))                     # [[1, 3]]
    print(sol.findMissingRanges([1, 2, 3], 1, 3))              # []