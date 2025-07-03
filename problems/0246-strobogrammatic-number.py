# LeetCode 246 - Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

# ✅ Problem:
# Given a string num, return true if num is strobogrammatic.

# Strobogrammatic numbers look the same when rotated 180 degrees.
# Valid digit mappings:
# '0' ↔ '0', '1' ↔ '1', '6' ↔ '9', '8' ↔ '8', '9' ↔ '6'

# 🔍 Core Idea:
# Use two pointers (left and right) to compare mirrored characters.
# For each position, the left digit must match the rotated value of the right digit.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📚 Pattern: Two Pointers

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mappings = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in mappings or mappings[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True

# 🔄 Dry Run:
# Input: num = "69"
# mappings: {'6': '9'} → ✅
# pointers move inwards → done → return True

# Input: num = "962"
# mappings: {'6': '9'} vs '2' → '2' is invalid → return False

# 📌 Common Gotchas:
# - Must check if num[left] is a valid strobogrammatic digit.
# - Always compare num[left] to mappings[num[right]].

# 🧠 Memory Hook:
# two pointers → mapping digits → must match rotation → invalid if digit not in mappings