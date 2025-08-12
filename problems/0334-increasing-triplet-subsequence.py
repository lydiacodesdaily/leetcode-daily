# LeetCode 334 - Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
# (Not DP; classic greedy. Good live-interview pick.)

# ✅ Problem:
# Return True if there exist i < j < k with nums[i] < nums[j] < nums[k].

# 📚 Pattern:
# Greedy thresholds

# 🔍 Core Idea:
# Track two thresholds:
#   first  = smallest value seen so far
#   second = smallest value > first (best middle candidate)
# Scan left→right:
#   - If x <= first:  first = x               (start a better triplet)
#   - elif x <= second: second = x            (tighten the middle)
#   - else: x > second → we have first < second < x → return True

# 🧠 Memory Hook:
# keep two mins: first, second
# x <= first  → replace first
# else if x <= second → replace second
# else → third found → True

# ✅ Time: O(n)
# ✅ Space: O(1)

# 📌 Common Gotchas:
# - This is NOT about longest-increasing-subsequence counts; no resets of a length counter.
# - Use `<=` when updating first/second to keep them as small as possible (handles duplicates).
# - Never “reset” second when first drops—just keep shrinking them greedily as rules say.

from math import inf
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf, inf

        for x in nums:
            if x <= first:
                # Best (smallest) start so far
                first = x
            elif x <= second:
                # Best (smallest) middle so far given current first
                second = x
            else:
                # x > second ⇒ first < second < x
                return True

        return False


# 🔄 Dry Runs:
# 1) nums = [2, 1, 5, 0, 4, 6]
#    first=inf, second=inf
#    x=2  → first=2
#    x=1  → first=1            (better start)
#    x=5  → second=5
#    x=0  → first=0            (even better start; second stays 5)
#    x=4  → second=4           (tighten middle to 4)
#    x=6  → 6 > second(4) → True (0 < 4 < 6)

# 2) nums = [5, 4, 3, 2, 1] → strictly decreasing
#    first shrinks each time; second never set → False

# 3) nums = [1, 2, 2, 2, 3]
#    first=1, second=2, x=2 (ties keep second=2), x=3 → 3>2 → True