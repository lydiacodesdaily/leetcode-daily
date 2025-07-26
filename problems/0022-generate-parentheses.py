# LeetCode 22 - Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

# ✅ Problem:
# Given n pairs of parentheses, generate all combinations of well-formed parentheses.

# 📚 Pattern: Backtracking

# 🔍 Core Idea:
# At each step → we can add '(' if open < n → we can add ')' if close < open.
# Recursively explore all valid possibilities.

# 🧠 Memory Hook:
# backtrack → can add '(' if open < n → can add ')' if close < open → valid when open == close == n

# ✅ Time Complexity: O(4^n / √n)  (Catalan number)
# ✅ Space Complexity: O(n) recursion depth

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                res.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return res

# 🔄 Dry Run Example:
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]