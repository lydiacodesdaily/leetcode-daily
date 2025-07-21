# LeetCode 1891 - Cutting Ribbons
# https://leetcode.com/problems/cutting-ribbons/

# ✅ Problem:
# Given an array of ribbon lengths and an integer k, return the maximum length 
# each piece can be cut to so that we have at least k ribbon pieces.

# 📚 Pattern:
# Binary Search on Answer (Search Space)

# 🔍 Key Insight:
# - Search over possible piece lengths: from 1 to max(ribbons)
# - For each length `mid`, check if we can get at least k pieces
# - If yes → try longer lengths (move right); if not → try shorter lengths

# 🧠 Memory Hook:
# binary search on length
# can_cut = sum(r // length) ≥ k
# left = 1, right = max(ribbons)
# if can_cut → go right (left = mid + 1)
# else → go left (right = mid - 1)
# return right (last valid length)

# ✅ Time Complexity: O(n * log(max(ribbons)))
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Don't binary search the index — you're searching the possible lengths
# - Off-by-one in the binary search (should return `right` not `left`)
# - Always check `mid` in feasibility function, not `ribbons[mid]`

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # 🧪 Feasibility function: can we cut at least k pieces of length `length`?
        def can_cut(length: int) -> bool:
            return sum(r // length for r in ribbons) >= k

        # 🔍 Search space is lengths from 1 to max ribbon length
        left, right = 1, max(ribbons)
        res = 0

        # 🧭 Binary Search
        while left <= right:
            mid = (left + right) // 2

            if can_cut(mid):
                res = mid           # ✅ record this as current best
                left = mid + 1      # try longer lengths
            else:
                right = mid - 1     # try shorter lengths

        return res

# 🔄 Dry Run:
# ribbons = [9,7,5], k = 3
# left = 1, right = 9
# mid = 5 → [9//5=1, 7//5=1, 5//5=1] → total = 3 ✅
# → try longer: left = 6
# mid = 7 → [9//7=1, 7//7=1, 5//7=0] → total = 2 ❌
# → try shorter: right = 6
# mid = 6 → [9//6=1, 7//6=1, 5//6=0] → total = 2 ❌
# → try shorter: right = 5
# return right = 5 ✅