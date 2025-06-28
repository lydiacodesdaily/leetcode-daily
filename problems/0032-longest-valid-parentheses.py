# LeetCode 32 - Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

# ✅ Problem:
# Given a string s containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.

# 📚 Pattern: Stack (Index Tracking)

# 🔍 Core Idea:
# Use a stack to track **indexes**.
# When a valid window is closed → calculate its length → track the max.
# Push unmatched ')' index as base reset point.

# 🧠 Memory Hook:
# stack tracks indexes → pop on ')' → empty stack? → push index as reset
# max_len = max(max_len, i - stack[-1])

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # =========================
        # 🧱 Step 1: Initialize
        # =========================
        stack = [-1]  # Sentinel index → base for valid window calculation
        max_len = 0

        # =========================
        # 🔁 Step 2: Iterate string
        # =========================
        for i, c in enumerate(s):
            if c == '(':
                # ✅ Push index of '(' → possible start of valid window
                stack.append(i)
            else:
                # ✅ Try to match with previous '('
                stack.pop()

                if not stack:
                    # 🚨 Unmatched ')' → reset base → push current index
                    stack.append(i)
                else:
                    # ✅ Valid window → update max length
                    max_len = max(max_len, i - stack[-1])

        # =========================
        # ✅ Step 3: Return result
        # =========================
        return max_len

# 🔄 Dry Run:
# Input: ")()())"
# i = 0 → ')' → pop → stack empty → push index 0 → stack = [0]
# i = 1 → '(' → push index 1 → stack = [0, 1]
# i = 2 → ')' → pop → valid window → max_len = max(0, 2 - 0) = 2
# i = 3 → '(' → push index 3 → stack = [0, 3]
# i = 4 → ')' → pop → valid window → max_len = max(2, 4 - 0) = 4
# i = 5 → ')' → pop → stack empty → push index 5 → stack = [5]
# Final Answer: 4