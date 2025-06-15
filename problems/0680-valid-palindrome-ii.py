# LeetCode 680 - Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

# ✅ Problem:
# Given a string s, return true if the s can be a palindrome after deleting at most one character.

# 🔍 Key Insight:
# Use the **Two Pointers** technique to compare characters from both ends.
# If a mismatch occurs, try skipping either the left or right character.
# Then check if either resulting substring is a palindrome.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping left or right
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1

        return True
    
"""
s = "abca"
→ mismatch at s[0] = 'a' and s[3] = 'a' ✅
→ mismatch at s[1] = 'b' and s[2] = 'c' ❌
Try:
- skip s[1]: "aca" → ✅ is palindrome
- skip s[2]: "aba" → ✅ is palindrome
→ return True
"""