# LeetCode 1539 - Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/

# ✅ Problem:
# Given a sorted list of unique positive integers and an integer k,
# return the k-th missing positive number.

# 🧩 Base Pattern:
# Binary Search on Answer Space / Condition
# - We're not looking for a specific number in the array.
# - We're finding the **first index where the number of missing elements ≥ k**.

# 🧪 Subtype:
# Offset-based Binary Search on "missing count"
# - Since the array is strictly increasing, we know how many numbers **should** be there at index `i`: (i + 1)
# - But the actual number is `arr[i]`, so the difference tells us how many are missing.
#     missing = arr[i] - (i + 1)

# 🧠 Memory Hook:
# binary search: first index where missing >= k
# missing = actual - ideal → arr[i] - (i + 1)
# return left + k

# 🔍 Key Insight:
# For a given index `i`, the number of missing integers before `arr[i]` is:
#     arr[i] - (i + 1)
# If this missing count < k, go right; otherwise, go lef

# ✅ Time Complexity: O(log n) - binary search
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Confusing “missing count” formula → arr[i] - (i + 1)
# - Using wrong return formula (don’t return arr[mid] or arr[left])
# - This is not a standard binary search on value — it's on count gap

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        # 🧭 Binary search for first index where missing >= k
        while left <= right:
            mid = (left + right) // 2

            # Calculate how many numbers are missing before index mid
            # Ideal: index i should have value (i + 1), so missing = actual - ideal
            missing = arr[mid] - (mid + 1)

            if missing < k:
                # Not enough missing numbers yet — move right
                left = mid + 1
            else:
                # Too many missing — move left
                right = mid - 1

        # ✅ Final answer = left + k
        return left + k

# 🔄 Dry Run:
# Input: arr = [2,3,4,7,11], k = 5
# Missing counts:
# i = 0 → 2 - (0+1) = 1
# i = 1 → 3 - (1+1) = 1
# i = 2 → 4 - (2+1) = 1
# i = 3 → 7 - (3+1) = 3
# i = 4 → 11 - (4+1) = 6

# Goal: find first i where missing >= 5 → index = 4
# So return: left + k = 4 + 5 = 9 ✅