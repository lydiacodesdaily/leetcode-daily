# LeetCode 1060 - Missing Element in Sorted Array
# https://leetcode.com/problems/missing-element-in-sorted-array/
# ✅ Problem:
# Given a sorted array of unique integers and a number k,
# return the k-th missing number starting from the first element.

# 🧩 Pattern:
# Binary Search on Answer Space

# 🔍 Key Insight:
# For index i, number of missing elements from nums[0] to nums[i] is:
#     missing = nums[i] - nums[0] - i
# Use binary search to find the smallest index where missing >= k

# 🧠 Memory Hook:
# missing = nums[i] - nums[0] - i
# binary search for first i where missing ≥ k
# return nums[left - 1] + (k - missing[left - 1])

# ✅ Time Complexity: O(log n)
# ✅ Space Complexity: O(1)

# 📌 Gotchas:
# - Avoid looping through full range → too slow
# - Watch out for off-by-one errors at the end

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(idx):
            # How many numbers are missing until index `idx`
            return nums[idx] - nums[0] - idx

        n = len(nums)
        
        # 🧭 Binary search to find the first index where missing(idx) >= k
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        # 🔚 After binary search:
        # left is the first index where missing(left) >= k
        # We need to go back one step and compute how many more to go
        return nums[left - 1] + (k - missing(left - 1))

# 🔄 Dry Run:
# Input: nums = [4,7,9,10], k = 3
# missing(0) = 0
# missing(1) = 7-4-1 = 2
# missing(2) = 9-4-2 = 3
# binary search finds index 2
# answer = nums[1] + (k - missing(1)) = 7 + (3 - 2) = 8 ✅