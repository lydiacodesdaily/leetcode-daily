# LeetCode 20 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# ✅ Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.

# 🔍 Core Idea:
# Use a stack to match each closing bracket with its corresponding opening bracket.
# Push opening brackets to stack; pop only if matching closing bracket is seen.

# 📚 Pattern:
# Stack + Hash Map (for matching brackets)

# 🧠 Memory Hook:
# push open → stack
# on close: if match top → pop
# if not match or stack empty → False
# if stack empty at end → True ✅

# ✅ Time Complexity: O(n) — single pass
# ✅ Space Complexity: O(n) — stack space in worst case

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # track opening brackets
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in pairs:
                # It's an opening bracket → push to stack
                stack.append(c)
            else:
                # It's a closing bracket → check match
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        # Valid only if all opened brackets are closed
        return not stack

# 🔄 Dry Run:
# Input: s = "({[]})"
# stack = [ ( → [(, { → [(, {, [ → [(, {, [
# ] matches top [ → pop → [(, {
# } matches top { → pop → [(
# ) matches top ( → pop → []
# ✅ Empty stack → valid = True