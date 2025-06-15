# LeetCode 1249 - Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# ✅ Problem:
# Given a string s of '(', ')' and lowercase English characters,
# remove the minimum number of parentheses so that the resulting string is valid.
# A string is valid if parentheses are balanced and well-ordered.

# 🔍 Key Insight:
# Do two passes:
# 1. First pass (left to right) to remove extra ')'
# 2. Second pass (right to left) to remove extra '('

# 🔁 Key Observations:
# - When scanning left to right:
#   • Keep track of open parentheses.
#   • Only allow ')' when open > 0.
# - When scanning right to left:
#   • Keep track of close parentheses.
#   • Only allow '(' when close > 0.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n) to store the result string

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: Remove invalid ')' left > right
        result = []
        open_count = 0
        for char in s:
            if char == '(':
                open_count += 1
                result.append(char)
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                    result.append(char)
                # else: skip this invalid ')'
            else:
                result.append(char)

        # Second pass: Remove unmatched '(' from right to left
        final = []
        close_count = 0
        for char in reversed(result):
            if char == ')':
                close_count += 1
                final.append(char)
            elif char == '(':
                if close_count > 0:
                    close_count -= 1
                    final.append(char)
                # else: skip this invalid '('
            else:
                final.append(char)

        # Reverse to restore original order
        return ''.join(reversed(final))

# 🔄 Dry Run:
# Input: "a)b(c)d"
# Pass 1 result: ['a', 'b', '(', 'c', ')', 'd'] → removed first ')'
# Pass 2 reversed: ['d', ')', 'c', '(', 'b', 'a'] → no extra '('
# Final output: "ab(c)d"

# 🗋 Pattern: Stack Simulation / Two-Pass Greedy
# 🔌 Alternative: Could be solved with a real stack and index tracking, but two-pass is cleaner

# 📌 Common Gotchas:
# - Not reversing the second pass
# - Off-by-one errors in parentheses counting
# - Forgetting to append non-parenthesis characters

# 📂 Suitable for: Easy-Medium level interview, often used to test parsing, balancing, and greedy passes
