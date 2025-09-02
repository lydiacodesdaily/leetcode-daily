# LeetCode 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# ✅ Problem:
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Do it without converting the integer to a string.

# 📚 Pattern:
# Math (reverse half of the number)

# 🔍 Core Idea:
# - Negative numbers are never palindrome (leading '-').
# - Numbers ending with 0 are not palindrome unless the number is 0.
# - Reverse only the *second half* of the number:
#   - Keep dividing x by 10
#   - Build reversed_half by adding last digit each step
#   - Stop when reversed_half >= x
# - Compare:
#   - Even length → x == reversed_half
#   - Odd length  → x == reversed_half // 10 (drop the middle digit)

# 🧠 Memory Hook:
# reverse half only
# stop when reversed >= x
# compare x vs reversed or reversed//10

# ✅ Time Complexity: O(log n) → digits processed
# ✅ Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # ❌ Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        # keep building reversed_half until it's >= remaining x
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # ✅ For even length: x == reversed_half
        # ✅ For odd length: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10


# -------------------------------
# 🔄 Dry Runs
# -------------------------------

# Example 1: x=1221 (even length)
# reversed_half=0
# loop1: x=122, reversed=1
# loop2: x=12,  reversed=12
# loop stops (x=12, reversed=12)
# compare → x == reversed → True

print(Solution().isPalindrome(1221))  # ✅ True

# Example 2: x=12321 (odd length)
# reversed_half=0
# loop1: x=1232, reversed=1
# loop2: x=123,  reversed=12
# loop3: x=12,   reversed=123
# stop (x=12, reversed=123)
# compare → x == reversed//10 (12 == 12) → True

print(Solution().isPalindrome(12321))  # ✅ True

# Example 3: x=-121 → immediate False
print(Solution().isPalindrome(-121))   # ✅ False

# Example 4: x=10 → not palindrome
print(Solution().isPalindrome(10))     # ✅ False