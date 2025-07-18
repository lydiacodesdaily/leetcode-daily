# LeetCode 125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# ✅ Problem:
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# 📚 Pattern:
# Two Pointers

# 🔍 Core Idea:
# Use two pointers (left and right) to scan the string from both ends toward the center.
# Skip non-alphanumeric characters and compare lowercased characters.
# If all characters match → it's a palindrome.

# 🧠 Memory Hook:
# two pointers → skip non-alphanumeric  
# compare lowercased chars → if mismatch → return False  
# return True if pointers cross

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting to lowercase characters
# - Not skipping non-alphanumeric characters correctly

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# 🔄 Dry Run:
# Input: "A man, a plan, a canal: Panama"
# Ignore non-alphanumeric → compare 'a' and 'a', 'm' and 'm', ..., all match → return True
#
# Input: "race a car"
# Compare → 'r' vs 'r', 'a' vs 'a', 'c' vs 'c', 'e' vs ' ' (skip space) → compare 'e' vs 'a' → return False