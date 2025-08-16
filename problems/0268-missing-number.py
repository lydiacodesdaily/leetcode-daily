# LeetCode 268 - Missing Number
# https://leetcode.com/problems/missing-number/
#
# ✅ Problem:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the one number in the range that is missing from the array.
#
# 📚 Pattern:
# Math / Bit Manipulation / Hash Set
#
# ✅ Time Complexity:
# - Set: O(n) time, O(n) space
# - Sum: O(n) time, O(1) space
# - XOR: O(n) time, O(1) space
# - Binary Search: O(n log n) time, O(1) space (after sort)
#
# 📌 Common Gotchas:
# - Range is [0..n], not [1..n]
# - Avoid O(n log n) unless sorting is given/allowed
# - In fixed-width integer languages, XOR avoids overflow risk

from typing import List

# 1️⃣ Set Lookup — Easiest to think of
class SolutionSet:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1  # total count including the missing number
        for number in range(n):
            if number not in num_set:
                return number


# 2️⃣ Sum Formula — Math trick
class SolutionSum:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


# 3️⃣ XOR — Interview favorite, avoids overflow in some languages
class SolutionXOR:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # XOR all indices [0..n]
        for i in range(n + 1):
            ans ^= i

        # XOR all values in nums
        for x in nums:
            ans ^= x

        return ans


# 4️⃣ Binary Search — Only if nums is sorted or sorting is allowed
class SolutionBinarySearch:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)  # search space [0..n]
        while left < right:
            mid = (left + right) // 2
            if mid < len(nums) and nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left


# 🔄 Dry Run (XOR example)
# nums = [3,0,1] (n=3)
# XOR all indices: 0^1^2^3 = 0
# XOR all nums: 0^3=3, 3^0=3, 3^1=2 → missing number = 2 ✅