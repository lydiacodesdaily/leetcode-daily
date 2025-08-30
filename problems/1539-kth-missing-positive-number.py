# LeetCode 1539 - Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/
#
# ✅ Problem:
# Given a sorted list of unique positive integers `arr` and an integer k,
# return the kth missing positive integer.
#
# 📚 Pattern:
# Binary Search on Answer Space → Lower Bound
#
# 🔍 Key Insight:
# - For index i, number of missing = arr[i] - (i + 1).
# - This sequence is non-decreasing.
# - We want the first index where missing(i) ≥ k → classic lower_bound.
# - Final answer = left + k.
#
# 🧠 Memory Hook:
# missing = actual - ideal → arr[i] - (i+1)
# lower_bound(missing >= k)
# return left + k
#
# ✅ Time Complexity: O(log n)
# ✅ Space Complexity: O(1)
#
# 📌 Common Gotchas:
# - Must set right = n (one past end) for half-open [left,right).
# - Don’t use equality check (missing == k), it can skip the answer.
# - Return formula is not arr[left] or arr[mid]; it’s left + k.
#
# 🔄 Dry Run:
# arr = [2,3,4,7,11], k=5
# missing: [1,1,1,3,6]
# left=0, right=5
# mid=2 → missing=1<5 → left=3
# mid=4 → missing=6≥5 → right=4
# mid=3 → missing=3<5 → left=4
# loop ends: left=4
# answer = 4+5 = 9 ✅

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n  # half-open range [0, n)

        def missing(i: int) -> int:
            return arr[i] - (i + 1)

        # lower_bound: first index with missing(i) >= k
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left + k