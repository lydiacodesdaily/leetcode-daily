# LeetCode 169 - Majority Element
# https://leetcode.com/problems/majority-element/

# ✅ Problem:
# Given an array nums of size n, return the element that appears more than ⌊n / 2⌋ times.
# It is guaranteed that the majority element exists.

# 📚 Pattern:
# Greedy / Boyer-Moore Voting Algorithm

# 🔍 Key Insight:
# - Since majority element appears more than n/2 times, all other elements together
#   cannot cancel it out completely.
# - Track a candidate and a vote count. Replace candidate if count is 0.

# 🧠 Memory Hook:
# count = 0 → set candidate
# match → count++
# no match → count--

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


# 🔄 Dry Run:
# Input: [2,2,1,1,1,2,2]
# Steps:
# 2 → candidate = 2, count = 1
# 2 → same → count = 2
# 1 → diff → count = 1
# 1 → diff → count = 0 → reset
# 1 → candidate = 1, count = 1
# 2 → diff → count = 0 → reset
# 2 → candidate = 2, count = 1
# ✅ Output: 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([2,2,1,1,1,2,2]))  # Output: 2
    print(sol.majorityElement([3,3,4]))          # Output: 3
    print(sol.majorityElement([1]))              # Output: 1